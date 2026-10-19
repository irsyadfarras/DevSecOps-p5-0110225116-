import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)

    def test_calculate(self):
        response = self.client.post('/api/calculate', json={"num1": 5, "num2": 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 15)

if __name__ == '__main__':
    unittest.main()
