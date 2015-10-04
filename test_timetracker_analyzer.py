import unittest
import timetracker_analyzer as analyzer

from datetime import timedelta


class TestTimeTrackerAnalyzer(unittest.TestCase):

    def test_get_month_year_perfect(self):
        self.assertEqual("October - 2015",
                         analyzer.get_month_year("2015-10-03 19:08:30"))

    def test_get_month_year_empty(self):
        self.assertRaises(ValueError,
                          analyzer.get_month_year,
                          "")

    def test_get_timedelta_perfect(self):
        expected = timedelta(seconds=9)
        self.assertEqual(expected,
                         analyzer.get_timedelta("2015-10-03 19:08:30",
                                                 "2015-10-03 19:08:39"))

    def test_get_timedelta_empty(self):
        self.assertRaises(ValueError,
                          analyzer.get_timedelta,
                          "2015-10-03 19:08:30",
                          "")

    def test_get_timedelta_negative(self):
        self.assertRaises(ValueError,
                          analyzer.get_timedelta,
                          "2015-10-03 19:08:30",
                          "2015-10-03 19:08:00")

if __name__ == '__main__':
    unittest.main()
