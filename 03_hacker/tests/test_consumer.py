import argparse
import json
import unittest
from unittest.mock import patch, MagicMock
from hacker.consumer import consume


class TestConsumer(unittest.TestCase):
    @patch('consumer.redis.StrictRedis')
    def test_consume_swap(self, mock_redis):
        mock_pubsub = MagicMock()
        mock_pubsub.listen.return_value = iter([
            {'type': 'message', 'data': json.dumps({
                'metadata': {'from': '1234567890', 'to': '0987654321'},
                'amount': 5000
            })}
        ])
        mock_redis.return_value.pubsub.return_value = mock_pubsub

        with patch('consumer.parse_arguments', return_value=argparse.Namespace(evils='0987654321')):
            consume('0987654321')

        mock_pubsub.listen.assert_called_once()

    @patch('consumer.redis.StrictRedis')
    def test_consume_non_swap(self, mock_redis):
        mock_pubsub = MagicMock()
        mock_pubsub.listen.return_value = iter([
            {'type': 'message', 'data': json.dumps({
                'metadata': {'from': '1234567890', 'to': '0987654322'},
                'amount': 5000
            })}
        ])
        mock_redis.return_value.pubsub.return_value = mock_pubsub

        with patch('consumer.parse_arguments', return_value=argparse.Namespace(evils='0987654321')):
            consume('0987654321')

        mock_pubsub.listen.assert_called_once()

    @patch('consumer.redis.StrictRedis')
    def test_consume_negative(self, mock_redis):
        mock_pubsub = MagicMock()
        mock_pubsub.listen.return_value = iter([
            {'type': 'message', 'data': json.dumps({
                'metadata': {'from': '1234567890', 'to': '0987654321'},
                'amount': -5000
            })}
        ])
        mock_redis.return_value.pubsub.return_value = mock_pubsub

        with patch('consumer.parse_arguments', return_value=argparse.Namespace(evils='0987654321')):
            consume('0987654321')

        mock_pubsub.listen.assert_called_once()


if __name__ == '__main__':
    unittest.main()
