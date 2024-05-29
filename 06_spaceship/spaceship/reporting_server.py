import grpc
from concurrent import futures
import spaceship_pb2
import spaceship_pb2_grpc
import random


class SpaceshipService(spaceship_pb2_grpc.SpaceshipServiceServicer):
    def GetSpaceships(self, request, context):
        print(request)

        # demo
        num_spaceships = random.randint(1, 10)

        for _ in range(num_spaceships):
            spaceship = spaceship_pb2.Spaceship()
            spaceship.alignment = random.choice(
                [spaceship_pb2.ALLY, spaceship_pb2.ENEMY])
            if spaceship.alignment == spaceship_pb2.ENEMY:
                spaceship.name = "Unknown"
            else:
                spaceship.name = random.choice([
                    'Moonrakers', 'Orion III',
                    'Daedalus', 'Explorer',
                    'Excalibur', 'Odyssey',
                    'Pleiades', 'Roger',
                    'Bebop', 'Firefly',
                    'Normandy', 'Millennium Falcon'])
            spaceship.ship_class = random.choice([
                spaceship_pb2.CORVETTE,
                spaceship_pb2.FRIGATE,
                spaceship_pb2.CRUISER,
                spaceship_pb2.DESTROYER,
                spaceship_pb2.CARRIER,
                spaceship_pb2.DREADNOUGHT
            ])
            spaceship.length = random.uniform(80.0, 20000.0)
            spaceship.crew_size = random.randint(4, 500)
            spaceship.armed = random.choice([True, False])
            if spaceship.alignment == spaceship_pb2.ENEMY:
                yield spaceship
                continue
            names = ["John", "Jane", "David", "Emily", "Michael", "Jack"]
            surnames = ["Doe", "Smith", "Johnson",
                        "Brown", "Taylor", "Shepard"]
            ranks = ["Ensign", "Lieutenant", "Captain", "Admiral", "Commander"]

            num_officers = random.randint(1, 10)
            for _ in range(num_officers):
                officer = spaceship.officers.add()
                officer.first_name = random.choice(names)
                officer.last_name = random.choice(surnames)
                officer.rank = random.choice(ranks)

            yield spaceship


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    print('Server started!')
    spaceship_pb2_grpc.add_SpaceshipServiceServicer_to_server(
        SpaceshipService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
