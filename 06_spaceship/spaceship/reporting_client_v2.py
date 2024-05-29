# | Class       | Length     | Crew    | Can be armed? | Can be hostile? |
# |-------------|------------|---------|---------------|-----------------|
# | CORVETTE    | 80-250     | 4-10    | Yes           | Yes             |
# | Frigate     | 300-600    | 10-15   | Yes           | No              |
# | Cruiser     | 500-1000   | 15-30   | Yes           | Yes             |
# | Destroyer   | 800-2000   | 50-80   | Yes           | No              |
# | Carrier     | 1000-4000  | 120-250 | No            | Yes             |
# | Dreadnought | 5000-20000 | 300-500 | Yes           | Yes             |

from typing import List
import grpc
import sys
import spaceship_pb2_grpc
import spaceship_pb2
from pydantic import BaseModel, field_validator


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


class Spaceship(BaseModel):
    name: str
    ship_class: str
    alignment: str
    length: float
    crew_size: int
    armed: bool
    officers: List[Officer]

    @field_validator('alignment')
    def validate_alignment(cls, alignment, values):
        allowed_alignment_values = {
            'FRIGATE': 'ENEMY',
            'DESTROYER': 'ENEMY',
        }
        ship_class = values.data['ship_class']
        if ship_class not in allowed_alignment_values:
            return alignment
        if alignment != allowed_alignment_values[ship_class]:
            raise ValueError(
                f"Invalid armed value for {ship_class}. Must be {allowed_alignment_values[ship_class]}")
        return alignment

    @field_validator('length')
    def validate_length(cls, length, values):
        allowed_ranges = {
            'CORVETTE': (80, 250),
            'FRIGATE': (300, 600),
            'CRUISER': (500, 1000),
            'DESTROYER': (800, 2000),
            'CARRIER': (1000, 4000),
            'DREADNOUGHT': (5000, 20000)
        }
        ship_class = values.data['ship_class']
        if ship_class in allowed_ranges and (length < allowed_ranges[ship_class][0] or length > allowed_ranges[ship_class][1]):
            raise ValueError(
                f"Invalid length for {ship_class}. Must be within the range {allowed_ranges[ship_class]}")
        return length

    @field_validator('crew_size')
    def validate_crew_size(cls, crew_size, values):
        allowed_ranges = {
            'CORVETTE': range(4, 11),
            'FRIGATE': range(10, 16),
            'CRUISER': range(15, 31),
            'DESTROYER': range(50, 81),
            'CARRIER': range(120, 251),
            'DREADNOUGHT': range(300, 501)
        }
        ship_class = values.data['ship_class']
        if ship_class not in allowed_ranges:
            return crew_size
        if crew_size not in allowed_ranges[ship_class]:
            raise ValueError(
                f"Invalid crew size for {ship_class}. Must be within {allowed_ranges[ship_class]}")
        return crew_size

    @field_validator('armed')
    def validate_armed(cls, armed, values):
        allowed_armed_values = {
            'CORVETTE': True,
            'FRIGATE': True,
            'CRUISER': True,
            'DESTROYER': True,
            'CARRIER': False,
            'DREADNOUGHT': True
        }
        ship_class = values.data['ship_class']
        if ship_class not in allowed_armed_values:
            return armed
        if armed != allowed_armed_values[ship_class]:
            raise ValueError(
                f"Invalid armed value for {ship_class}. Must be {allowed_armed_values[ship_class]}")
        return armed


def run(coordinates):
    latitude = coordinates[0]
    longitude = coordinates[1]

    try:
        latitude = float(latitude.replace('−', '-'))
        longitude = float(longitude.replace('−', '-'))
    except ValueError:
        print("Invalid coordinates. Latitude and longitude must be numeric values.")
        return

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spaceship_pb2_grpc.SpaceshipServiceStub(channel)
        request = spaceship_pb2.Coordinates(
            latitude=latitude,
            longitude=longitude
        )
        spaceship_list = []
        try:
            for spaceship in stub.GetSpaceships(request):
                spaceship_dict = {
                    "alignment": spaceship_pb2.Alignment.Name(spaceship.alignment),
                    "name": spaceship.name,
                    "ship_class": spaceship_pb2.ShipClass.Name(spaceship.ship_class),
                    "length": spaceship.length,
                    "crew_size": spaceship.crew_size,
                    "armed": spaceship.armed,
                    "officers": []
                }

                for officer in spaceship.officers:
                    officer_dict = {
                        "first_name": officer.first_name,
                        "last_name": officer.last_name,
                        "rank": officer.rank
                    }
                    spaceship_dict["officers"].append(officer_dict)
                try:
                    validated_spaceship = Spaceship(**spaceship_dict)
                    spaceship_json = validated_spaceship.model_dump_json()
                    spaceship_list.append(spaceship_json)
                except ValueError as e:
                    # print(f"Invalid spaceship: {e}")
                    continue

        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                print("RPC Cancelled")
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                print("RPC Unavailable")
            else:
                print("RPC Error", e.code(), e.details())

        for spaceship_json in spaceship_list:
            print(spaceship_json)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: reporting_client.py latitude longitude")
    else:
        coordinates = sys.argv[1:3]
        run(coordinates)
