import unittest
import json
from flask import Flask
from server.py import app  # Import your Flask app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Configure your app for testing
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_predict(self):
        # Send a POST request to the /predict endpoint with test data
        test_data = {
            'age': 45, 'al': 1, 'su': 0, 'bgr': 150, 'bu': 36, 'sc': 1.2, 'sod': 138, 'pcv': 44, 'rc': 5.2, 'htn': 'yes'
        }
        response = self.app.post('/predict', json=test_data)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response contains a prediction
        response_data = json.loads(response.data)
        self.assertTrue('prediction' in response_data)

if __name__ == '__main__':
    unittest.main()
