#pytest 
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

if __name__ == '__main__':
    unittest.main()
