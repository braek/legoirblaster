from unittest import TestCase
from unittest.mock import MagicMock
import subprocess
from .. import constants
from ..app import app


class AppTests(TestCase):
    """
    Unit tests for the Flask application itself
    """
    def setUp(self):
        self.app = app.test_client()
        AppTests.call_method_backup = subprocess.call

    def tearDown(self):
        subprocess.call = AppTests.call_method_backup

    def test_get_index_http_ok(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_get_index_http_ok_content_type(self):
        response = self.app.get('/')
        self.assertEqual(response.content_type, constants.HTML_CONTENT_TYPE)

    def test_post_index_http_not_allowed(self):
        response = self.app.post('/')
        self.assertEqual(405, response.status_code)

    def test_get_send_command_http_not_allowed(self):
        response = self.app.get('/send-command')
        self.assertEqual(405, response.status_code)

    def test_post_send_command_http_not_allowed_with_invalid_speed_content_type(self):
        response = self.app.post('/send-command', data={
            'speed': 8,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(constants.JSON_CONTENT_TYPE, response.content_type)

    def test_post_send_command_http_not_allowed_with_invalid_speed(self):
        response = self.app.post('/send-command', data={
            'speed': 8,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_http_not_allowed_with_invalid_channel(self):
        response = self.app.post('/send-command', data={
            'speed': 7,
            'channel': 5,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_http_not_allowed_with_invalid_output(self):
        response = self.app.post('/send-command', data={
            'speed': 7,
            'channel': 4,
            'output': 'G'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_http_bad_request_with_invalid_brake_value(self):
        response = self.app.post('/send-command', data={
            'brake': 'abc',
            'speed': 1,
            'channel': 123,
            'output': 'ABC'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_http_bad_request_with_invalid_speed_value(self):
        response = self.app.post('/send-command', data={
            'brake': 0,
            'speed': 'abc',
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_http_bad_request_with_invalid_channel_value(self):
        response = self.app.post('/send-command', data={
            'brake': 0,
            'speed': 1,
            'channel': 'abc',
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_http_ok_with_valid_command(self):
        subprocess.call = MagicMock()
        response = self.app.post('/send-command', data={
            'speed': 1,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(200, response.status_code)

    def test_post_send_command_http_internal_server_error_with_invalid_lirc_installation(self):
        subprocess.call = MagicMock(side_effect=FileNotFoundError)
        response = self.app.post('/send-command', data={
            'speed': 1,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(500, response.status_code)
