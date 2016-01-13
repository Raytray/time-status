import time_api_controller
import unittest

from datetime import datetime as dt


class TestTimeAPIController(unittest.TestCase):
    def setUp(self):
        self.app = time_api_controller.app.test_client()
        self.date_format = '%Y-%m-%d'

    def test_index_status(self):
        assert self.app.get('/').status_code == 200

    def test_index_response_type(self):
        assert self.app.get('/').content_type == 'text/html; charset=utf-8'

    def test_data_status(self):
        assert self.app.get('/api/time-series').status_code == 200

    def test_data_response(self):
        assert self.app.get(
            '/api/time-series').content_type == 'application/json'

    def test_data_arguments_category(self):
        assert self.app.get('/api/time-series?category=test').status_code == 200

    def test_data_arguments_start_date(self):
        assert self.app.get(
            '/api/time-series?start_date=2015-01-31').status_code == 200

    def test_data_arguments_end_date(self):
        assert self.app.get(
            '/api/time-series?end_date=2015-01-31').status_code == 200

    def test_data_parameters_start_date(self):
        args = {'start_date': '2015-01-31'}
        result = {'Start time':
                  {'$gte': dt.strptime(args.get('start_date'),
                                       self.date_format)
               }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_end_date(self):
        args = {'end_date': '2015-01-31'}
        result = {'End time':
                  {'$lte': dt.strptime(args.get('end_date'),
                                       self.date_format)
               }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_start_and_end_date(self):
        args = {'start_date': '2015-01-31',
                'end_date': '2015-02-01'}
        result = {'End time':
                  {'$lte': dt.strptime(args.get('end_date'),
                                       self.date_format)},
                   'Start time':
                   {'$gte': dt.strptime(args.get('start_date'),
                                       self.date_format)
                }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_start_category(self):
        args = {'category': 'test'}
        result = {'Category': args.get('category')}
        assert time_api_controller.get_data_parameters(args) == result


if __name__ == '__main__':
    unittest.main()
