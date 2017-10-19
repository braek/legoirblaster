import unittest
from ..app import app


class AppTests(unittest.TestCase):
    """
    Unit tests for the Flask application itself
    """
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_index_http_ok(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_post_index_http_not_allowed(self):
        response = self.app.post('/')
        self.assertEqual(405, response.status_code)

    def test_get_cmd_not_allowed(self):
        response = self.app.get('/cmd')
        self.assertEqual(405, response.status_code)

    def test_post_cmd_not_allowed_with_invalid_speed(self):
        response = self.app.post('/cmd', data={
            'speed': 8,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_cmd_not_allowed_with_invalid_channel(self):
        response = self.app.post('/cmd', data={
            'speed': 7,
            'channel': 5,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_cmd_not_allowed_with_invalid_output(self):
        response = self.app.post('/cmd', data={
            'speed': 7,
            'channel': 4,
            'output': 'G'
        })
        self.assertEqual(405, response.status_code)

    def test_post_cmd_bad_request_with_invalid_brake_value(self):
        response = self.app.post('/cmd', data={
            'brake': 'abc',
            'speed': 1,
            'channel': 123,
            'output': 'ABC'
        })
        self.assertEqual(400, response.status_code)

    def test_post_cmd_bad_request_with_invalid_speed_value(self):
        response = self.app.post('/cmd', data={
            'brake': 1,
            'speed': 'abc',
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)

    def test_post_cmd_bad_request_with_invalid_channel_value(self):
        response = self.app.post('/cmd', data={
            'brake': 1,
            'speed': 1,
            'channel': 'abc',
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)
