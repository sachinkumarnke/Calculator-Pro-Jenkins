import os
import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def validate_number(value):
    """Validate and convert input to float, checking for NaN"""
    if value is None:
        raise ValueError("Number cannot be None")
    
    try:
        num = float(value)
    except TypeError:
        raise ValueError(f"Invalid type: expected number, got {type(value).__name__}")
    except ValueError:
        raise ValueError(f"Cannot convert '{value}' to number")
    
    if math.isnan(num):
        raise ValueError("NaN values are not allowed")
    if math.isinf(num):
        raise ValueError("Infinity values are not allowed")
    
    return num

def perform_operation(operation, num1, num2):
    """Perform calculation with pre-validated numbers"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

# Valid operations
VALID_OPERATIONS = {'add', 'subtract', 'multiply', 'divide'}

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # Extract values once to avoid repeated dictionary lookups
        num1_raw = data.get('num1')
        num2_raw = data.get('num2')
        operation = data.get('operation')
        
        if num1_raw is None or num2_raw is None or operation is None:
            return jsonify({'error': 'Missing required fields: num1, num2, operation'}), 400
            
        if operation not in VALID_OPERATIONS:
            return jsonify({'error': 'Invalid operation'}), 400
        
        # Validate numbers once
        num1 = validate_number(num1_raw)
        num2 = validate_number(num2_raw)
        
        result = perform_operation(operation, num1, num2)
        return jsonify({'result': result})
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except TypeError as e:
        return jsonify({'error': f'Type error: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'Unexpected error occurred'}), 500

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    if host == '0.0.0.0':
        host = '127.0.0.1'  # Force localhost for security
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)