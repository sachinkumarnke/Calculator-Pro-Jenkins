import unittest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app, validate_number, perform_operation

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_validate_number(self):
        self.assertEqual(validate_number(5), 5.0)
        self.assertEqual(validate_number('3.14'), 3.14)
        with self.assertRaises(ValueError):
            validate_number(None)
        with self.assertRaises(ValueError):
            validate_number('invalid')
    
    def test_perform_operation_add(self):
        self.assertEqual(perform_operation('add', 2, 3), 5)
        self.assertEqual(perform_operation('add', -1, 1), 0)
        self.assertEqual(perform_operation('add', 0, 0), 0)
    
    def test_perform_operation_subtract(self):
        self.assertEqual(perform_operation('subtract', 5, 3), 2)
        self.assertEqual(perform_operation('subtract', 0, 5), -5)
        self.assertEqual(perform_operation('subtract', 10, 10), 0)
    
    def test_perform_operation_multiply(self):
        self.assertEqual(perform_operation('multiply', 3, 4), 12)
        self.assertEqual(perform_operation('multiply', -2, 3), -6)
        self.assertEqual(perform_operation('multiply', 0, 5), 0)
    
    def test_perform_operation_divide(self):
        self.assertEqual(perform_operation('divide', 10, 2), 5)
        self.assertEqual(perform_operation('divide', 9, 3), 3)
        self.assertAlmostEqual(perform_operation('divide', 1, 3), 0.333333, places=5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            perform_operation('divide', 5, 0)
    
    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            perform_operation('invalid', 5, 3)
    
    def test_web_interface(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculator Pro', response.data)
    
    def test_api_calculate(self):
        response = self.app.post('/calculate',
                               data=json.dumps({'num1': 5, 'num2': 3, 'operation': 'add'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 8)
    
    def test_api_invalid_operation(self):
        response = self.app.post('/calculate',
                               data=json.dumps({'num1': 5, 'num2': 3, 'operation': 'invalid'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_api_missing_fields(self):
        response = self.app.post('/calculate',
                               data=json.dumps({'num1': 5}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()