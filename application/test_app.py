import unittest
from flask import url_for
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Web App with Python Flask!')

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Healthy...!!!')

    def test_invalid_url(self):
        response = self.app.get('/invalid_url')
        self.assertEqual(response.status_code, 404)

    def test_post_request(self):
        response = self.app.post('/post_request')
        self.assertEqual(response.status_code, 405)

    def test_redirect(self):
        response = self.app.get('/redirect')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], url_for('health', _external=True))

if __name__ == '__main__':
    unittest.main()
