# Instructions for ex01

> It is recommended to run always from Python [virtual environment](https://docs.python.org/3/library/venv.html).
>
> ```sh
> python -m venv /path/to/new/virtual/environment
> source <venv>/bin/activate
>```

- First, you need a Redis to be installed in your system. Here is the [instructions](https://redis.io/docs/getting-started/)
- Run Redis server:

    ```sh
    redis-server
    ```

- Install all required modules:

    ```sh
    pip install -r requirements.txt
    ```

- In the sake of testing `producer.py` won't generate multiple messages, not in an infinite loop either. So basically, this as "server" script needs to run first ideally, but we are not gonna do it.
- You need to run `consumer.py` script first that listens pubsub 'transactions'. So navigate to the `src` directory from a command line and run:

    ```sh
    python consumer.py -e 2222222222,44444444444
    ```

    Now consumer will listen what producer is going to send.

- Run the producer script:

    ```sh
    python producer.py
    ```

- At the end of it all stop Redis server:

    ```sh
    /etc/init.d/redis-server stop
    ```

## About testing

I tried to test both consumer and producer separately.

In `test_producer.py` we need to check that message has been generated succesfully and corresponds correct value.

In `test_consumer.py` we mock the message from producer and specifically swap the adresses.

To run those tests:

```sh
python -m unittest -v tests.test_producer
python -m unittest -v tests.test_consumer
```
