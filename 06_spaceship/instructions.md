# Day 06

Create venv:

```sh
python -m venv /path/to/new/virtual/environment
```

Install requirements:

```sh
pip install -r requirements.txt
```

Run the server:

```sh
python reporting_server.py
```

## ex00

Run client v1:

```sh
python reporting_client.py 174540.0409 −290028.118
```

## ex01

Run client with filter v2. Maybe it needs to adjust the number of generated ships in server(1000 instead of 10)

```sh
python reporting_client_v2.py 174540.0409 −290028.118
```
