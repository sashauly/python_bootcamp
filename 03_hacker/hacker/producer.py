import json
import logging
import random
import redis


logging.basicConfig(level=logging.INFO)


def generate_account_number():
    return str(random.randint(10**9, 10**10 - 1))


def produce():
    from_acccount = generate_account_number()
    to_account = generate_account_number()
    amount = random.randint(-10**4, 10**4)
    message = {
        "metadata": {
            "from": from_acccount,
            "to": to_account
        },
        "amount": amount
    }
    logging.info(json.dumps(message))
    return json.dumps(message)


if __name__ == '__main__':
    message = {
        "metadata": {
            "from": '1231231231',
            "to": '44444444444'
        },
        "amount": 10000
    }
    logging.info(json.dumps(message))
    produced_message = json.dumps(message)

    # produced_message = produce()

    redis_client = redis.StrictRedis()
    redis_client.publish('transactions', produced_message)
