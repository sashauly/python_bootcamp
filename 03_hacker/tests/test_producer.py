import unittest
import json
from hacker.producer import produce


class TestProducer(unittest.TestCase):
    def test_produce(self):
        message = produce()
        data = json.loads(message)
        self.assertIn('metadata', data)
        self.assertIn('from', data['metadata'])
        self.assertIn('to', data['metadata'])
        self.assertIn('amount', data)
        self.assertIsInstance(data['metadata']['from'], str)
        self.assertIsInstance(data['metadata']['to'], str)
        self.assertIsInstance(data['amount'], int)


if __name__ == '__main__':
    unittest.main()
