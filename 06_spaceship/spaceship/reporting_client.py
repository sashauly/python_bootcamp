import grpc
import spaceship_pb2
import spaceship_pb2_grpc
import sys
import json


def run(coordinates):
    latitude = coordinates[0]
    longitude = coordinates[1]

    # Input validation
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

                spaceship_json = json.dumps(spaceship_dict)
                spaceship_list.append(spaceship_json)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                print("RPC Cancelled")
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                print("RPC Unavailable")
            else:
                print("RPC Error", e.code(), e.details())

        # Print the spaceship JSON list
        for spaceship_json in spaceship_list:
            print(spaceship_json)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: reporting_client.py latitude longitude")
    else:
        coordinates = sys.argv[1:3]
        run(coordinates)
