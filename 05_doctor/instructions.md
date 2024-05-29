# README DAY 05

## Exercise 00

1. Run the server

    ```sh
    python credentials.py
    ```

2. Open second console, run curl(i don't get it why it often don't run in zsh, maybe my aliases stepped in a way. It worked in bash though!):

    ```sh
    curl http://127.0.0.1:8888/?species=Time%20Lord
    ```

## Exercise 01

- Step 1: Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

All files located in `wsgi` directory. So:

```sh
cd ./wsgi
```

To run the server and client applications, follow these steps:

- Step 2: Run the Server

    ```bash
    python server.py
    ```

    This will start the server on port 8888. You can open it in your browser on [address](http://127.0.0.1:8888/)

- Step 3: Run the Client

    To run the client, open a new terminal window and navigate to the directory containing the client script.

    To upload a file, use the following command:
    For example there's a test file in `wsgi` directory

    ```bash
    python screwdriver.py upload ./test.mp3
    ```

    To list all files on the server, use the following command:

    ```bash
    python screwdriver.py list
    ```

## Exercise 02

- Run the command:

    ```sh
    python doctors.py
    ```
