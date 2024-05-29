# Day 06 - Python Bootcamp

That Kind of Battle Training

protobuf, gRPC, Pydantic, SQLAlchemy

## Table of Contents

- [Day 06 - Python Bootcamp](#day-06---python-bootcamp)
  - [Table of Contents](#table-of-contents)
  - [Rules of the day](#rules-of-the-day)
  - [Tasks](#tasks)
    - [Exercise 00: Kirov Reporting (reporting\_client.py, reporting\_server.py)](#exercise-00-kirov-reporting-reporting_clientpy-reporting_serverpy)
    - [Exercise 01: Data Quality (reporting\_client\_v2.py)](#exercise-01-data-quality-reporting_client_v2py)
    - [Reading and tips](#reading-and-tips)

## Rules of the day

- You should turn in `*.py`, `*.proto` and `requirements.txt` files for this task. Also, optionally, config files and migrations for Alembic, if you decide to go for a bonus. You can also add a `README` file explaining how to start your application
- It is encouraged to write some tests for various cases inside your scripts as well. To make them run only when script is executed directly and not imported from somewhere else you can use `if __name__ == "__main__":` statement. You can read more about it [here](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

## Tasks

### Exercise 00: Kirov Reporting ([reporting_client.py](spaceship/reporting_client.py), [reporting_server.py](spaceship/reporting_server.py))

> Every spaceship had several characteristics:
>
>- Alignment (Ally/Enemy)
>- Name (can be "Unknown" for enemy ships)
>- Class, which is one of {Corvette, Frigate, Cruiser, Destroyer, Carrier, Dreadnought}
>- Length in meters
>- Size of the crew
>- Whether or not the ship is armed
>- One or more officers responsible for the ship
>
>It looked like the system should consist of three architectural layers:
>
>- Transport layer
>- Validation layer
>- Storage layer

The main protocol used for interspace communication was called "Protobuf 2.0". The entries were
being sent over the transport called "gRPC". So, this was the first layer Ender had to implement.

As gRPC is a client-server communication framework, two components had to be implemented -
`reporting_server.py` and `reporting_client.py`. The server should provide a response-streaming
endpoint, where it receives a set of coordinates (allowed to use [any particular system](https://en.wikipedia.org/wiki/Astronomical_coordinate_systems)), and responds with a stream of Spaceship entries.

As this is currently a test environment, even though every Spaceship should still have all the
parameters mentioned, they could be random. Also, they should be strictly typed, e.g.:

- Alignment is an enum
- Name is a string
- Length is a float
- Class is an enum
- Size is an integer
- Armed status is a bool
- Each officer on board should have first name, last name and rank as strings

The number of officers on board is a random number from 0 (for enemy ships only) to 10.

The workflow should go like this:

1) the server is started
2) the client is started given a set of coordinates in some chosen form, e.g.:

```bash
./reporting_client.py 17 45 40.0409 −29 00 28.118
```

  An example given is galactic coordinates for [Sagittarius A\*](https://en.wikipedia.org/wiki/Sagittarius_A*)

1) these coordinates are sent to the server, and server responds with a random (1-10) number
  of Spaceships in a gRPC stream to the client
1) the client prints to standard output all the received ships as a set of serialized JSON
  strings, like:

  ```json
  {
    "alignment": "Ally",
    "name": "Normandy",
    "class": "Corvette",
    "length": 216.3,
    "crew_size": 8,
    "armed": true,
    "officers": [
      {
        "first_name": "Alan",
        "last_name": "Shepard",
        "rank": "Commander"
      }
    ]
  }
  {
    "alignment": "Enemy",
    "name": "Executor",
    "class": "Dreadnought",
    "length": 19000.0,
    "crew_size": 450,
    "armed": true,
    "officers": []
  }
  ```

NOTE: this output here is formatted for readability, your code can still print one JSON per string

### Exercise 01: Data Quality ([reporting_client_v2.py](spaceship/reporting_client_v2.py))

List of classes with specific parameters:

| Class       | Length     | Crew    | Can be armed? | Can be hostile? |
|-------------|------------|---------|---------------|-----------------|
| Corvette    | 80-250     | 4-10    | Yes           | Yes             |
| Frigate     | 300-600    | 10-15   | Yes           | No              |
| Cruiser     | 500-1000   | 15-30   | Yes           | Yes             |
| Destroyer   | 800-2000   | 50-80   | Yes           | No              |
| Carrier     | 1000-4000  | 120-250 | No            | Yes             |
| Dreadnought | 5000-20000 | 300-500 | Yes           | Yes             |

The boy decided to represent these limitations as Pydantic data types (see [Reading](#reading-and-tips) section).

That way it will not just be easier to validate incoming data, but also serialization to JSON
becomes a lot easier. He decided to make another version of the client (`reporting_client_v2.py`),
which will work with the same server. But this time it should validate the stream of Spaceships
using Pydantic and filter out those which have some parameters out of bounds, according to the
table above. The rest should be printed exactly as in EX00.

Additionally, from the first part Ender already knew that Name could be "Unknown" ONLY for enemy
ships.

### Reading and tips

[Protocol Buffers using Python](https://developers.google.com/protocol-buffers/docs/pythontutorial)

[gRPC using Python](https://grpc.io/docs/languages/python/basics/)

[Pydantic Models](https://pydantic-docs.helpmanual.io/usage/models/)

[SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
