import unittest
import time_status as loader

from datetime import datetime as dt


class TestTimeStatus(unittest.TestCase):
    def setUp(self):
        date_format = "%Y-%m-%d %H:%M:%S"
        self._start_time = dt.strptime("2015-10-03 19:08:30", date_format)
        self._end_time = dt.strptime("2015-10-03 19:08:39", date_format)

    def test_get_timedelta_perfect(self):
        expected = 9.0
        self.assertEqual(expected,
                         loader.get_timedelta(self._start_time, self._end_time))

    def test_get_timedelta_empty(self):
        self.assertRaises(TypeError,
                          loader.get_timedelta,
                          self._start_time, None)

    def test_get_timedelta_negative(self):
        self.assertRaises(ValueError,
                          loader.get_timedelta, self._end_time,
                          self._start_time)

if __name__ == '__main__':
    unittest.main()
