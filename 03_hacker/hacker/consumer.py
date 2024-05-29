import argparse
import json
import logging
import redis

logging.basicConfig(level=logging.INFO, format='%(message)s')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", dest="evils",
                        required=True, type=str)
    return parser.parse_args().evils.split(',')


def consume(evil_accounts):
    r = redis.StrictRedis()
    pubsub = r.pubsub()
    pubsub.subscribe(['transactions'])

    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            metadata = data['metadata']

            sender = metadata['from']
            recipient = metadata['to']

            if recipient in evil_accounts and (data['amount'] >= 0):
                metadata['from'], metadata['to'] = recipient, sender
                logging.info('--->Swapped<---')
            logging.info(json.dumps(data))


if __name__ == "__main__":
    args = parse_arguments()
    consume(args)
    pass
