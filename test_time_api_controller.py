import time_api_controller
import unittest


class TestTimeAPIController(unittest.TestCase):
    def setUp(self):
        self.app = time_api_controller.app.test_client()

    def test_index_status(self):
        assert self.app.get('/').status_code == 200

    def test_index_response_type(self):
        assert self.app.get('/').content_type == 'text/html; charset=utf-8'

    def test_data_status(self):
        assert self.app.get('/api/time-series').status_code == 200

    def test_data_response(self):
        assert self.app.get(
            '/api/time-series').content_type == 'application/json'


if __name__ == '__main__':
    unittest.main()
