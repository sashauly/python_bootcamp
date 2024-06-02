import time
import unittest

from ex01.monotonic import monotonic


class MonotonicTestCase(unittest.TestCase):
    def test_monotonic(self):
        # Get the initial monotonic time
        initial_time = monotonic()

        # Wait for a short duration
        time.sleep(0.5)

        # Get the monotonic time again
        current_time = monotonic()

        # Verify that the current time is greater than the initial time
        self.assertGreater(current_time, initial_time)


if __name__ == '__main__':
    unittest.main()
