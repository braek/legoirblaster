import unittest
from unittest.mock import MagicMock
from ..app import app
import subprocess


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

    def test_get_send_command_not_allowed(self):
        response = self.app.get('/send-command')
        self.assertEqual(405, response.status_code)

    def test_post_send_command_not_allowed_with_invalid_speed(self):
        response = self.app.post('/send-command', data={
            'speed': 8,
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_not_allowed_with_invalid_channel(self):
        response = self.app.post('/send-command', data={
            'speed': 7,
            'channel': 5,
            'output': 'R'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_not_allowed_with_invalid_output(self):
        response = self.app.post('/send-command', data={
            'speed': 7,
            'channel': 4,
            'output': 'G'
        })
        self.assertEqual(405, response.status_code)

    def test_post_send_command_bad_request_with_invalid_brake_value(self):
        response = self.app.post('/send-command', data={
            'brake': 'abc',
            'speed': 1,
            'channel': 123,
            'output': 'ABC'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_bad_request_with_invalid_speed_value(self):
        response = self.app.post('/send-command', data={
            'brake': 0,
            'speed': 'abc',
            'channel': 1,
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_bad_request_with_invalid_channel_value(self):
        response = self.app.post('/send-command', data={
            'brake': 0,
            'speed': 1,
            'channel': 'abc',
            'output': 'R'
        })
        self.assertEqual(400, response.status_code)

    def test_post_send_command_ok_with_valid_command(self):
        call = subprocess.call
        subprocess.call = MagicMock()
        response = self.app.post('/send-command', data={
            'speed': 1,
            'channel': 1,
            'output': 'R'
        })
        subprocess.call = call
        self.assertEqual(200, response.status_code)

    def test_post_send_command_internal_server_error_with_invalid_lirc_installation(self):
        call = subprocess.call
        subprocess.call = MagicMock(side_effect=FileNotFoundError)
        response = self.app.post('/send-command', data={
            'speed': 1,
            'channel': 1,
            'output': 'R'
        })
        subprocess.call = call
        self.assertEqual(500, response.status_code)
