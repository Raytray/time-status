import unittest
import timetracker_analyzer as analyzer


class TestTimeTrackerAnalyzer(unittest.TestCase):

    def test_total_up_tasks(self):
        self.assertEqual(None,
                         analyzer.total_up_tasks('test', '00:00', '00:00'))

if __name__ == '__main__':
    unittest.main()
