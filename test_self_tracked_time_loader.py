import unittest
import self_tracked_time_loader as loader


class TestSelfTrackedTimeLoader(unittest.TestCase):
    def test_get_timedelta_perfect(self):
        expected = 9.0
        self.assertEqual(expected,
                         loader.get_timedelta("2015-10-03 19:08:30",
                                                 "2015-10-03 19:08:39"))

    def test_get_timedelta_empty(self):
        self.assertRaises(ValueError,
                          loader.get_timedelta,
                          "2015-10-03 19:08:30",
                          "")

    def test_get_timedelta_negative(self):
        self.assertRaises(ValueError,
                          loader.get_timedelta,
                          "2015-10-03 19:08:30",
                          "2015-10-03 19:08:00")

if __name__ == '__main__':
    unittest.main()
