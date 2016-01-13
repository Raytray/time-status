import time_api_controller
import unittest

from datetime import date, datetime
from dateutil.relativedelta import relativedelta


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
                  {'$gte': datetime.strptime(args.get('start_date'),
                                       self.date_format)
               }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_start_date_invalid(self):
        args = {'start_date': '2015-01-00'}
        result = {}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_end_date_invalid(self):
        args = {'end_date': '2015-01-00'}
        result = {}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_end_date(self):
        args = {'end_date': '2015-01-31'}
        result = {'End time':
                  {'$lte': datetime.strptime(args.get('end_date'),
                                       self.date_format)
               }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_start_and_end_date(self):
        args = {'start_date': '2015-01-31',
                'end_date': '2015-02-01'}
        result = {'End time':
                  {'$lte': datetime.strptime(args.get('end_date'),
                                       self.date_format)},
                   'Start time':
                   {'$gte': datetime.strptime(args.get('start_date'),
                                       self.date_format)
                }
        }
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_removes_end_date(self):
        args = {'period': '1y',
                'end_date': '2015-02-01'}
        period = date.today() + relativedelta(years=-1)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_years(self):
        args = {'period': '1y'}
        period = date.today() + relativedelta(years=-1)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_months(self):
        args = {'period': '1m'}
        period = date.today() + relativedelta(months=-1)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_days(self):
        args = {'period': '1d'}
        period = date.today() + relativedelta(days=-1)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_years_days(self):
        args = {'period': '1y2d'}
        period = date.today() + relativedelta(years=-1, days=-2)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_years_months(self):
        args = {'period': '1y2m'}
        period = date.today() + relativedelta(years=-1, months=-2)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_period_years_months_days(self):
        args = {'period': '1y3m2d'}
        period = date.today() + relativedelta(years=-1, months=-3, days=-2)
        result = {'Start time':
                  {'$gte': datetime.combine(period, datetime.min.time())}}
        assert time_api_controller.get_data_parameters(args) == result

    def test_data_parameters_category(self):
        args = {'category': 'test'}
        result = {'Category': args.get('category')}
        assert time_api_controller.get_data_parameters(args) == result

    def test_sanitize_match_group_none(self):
        assert time_api_controller.sanitize_match_group(None) == 0

    def test_sanitize_match_group_conversion(self):
        assert time_api_controller.sanitize_match_group("1") == 1


if __name__ == '__main__':
    unittest.main()
