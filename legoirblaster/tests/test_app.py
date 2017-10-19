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
