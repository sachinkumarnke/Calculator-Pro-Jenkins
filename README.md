# Python Jenkins CI/CD Pipeline

A simple Python calculator application with Jenkins CI/CD pipeline.

## Features
- Basic calculator operations (add, subtract, multiply, divide)
- Unit tests with pytest
- Jenkins pipeline automation

## Local Development
1. Create virtual environment: `python -m venv venv`
2. Activate environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `python -m pytest tests/`
5. Run application: `python main.py`

## Jenkins Pipeline
The pipeline includes:
- Code checkout from GitHub
- Virtual environment setup
- Dependency installation
- Unit test execution
- Application packaging
- Local deployment# Calculator-Pro-Jenkins
