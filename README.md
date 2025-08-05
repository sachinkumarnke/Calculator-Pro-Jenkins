# Calculator Pro - Jenkins CI/CD Pipeline

🧮 A professional Flask calculator application with automated Jenkins CI/CD pipeline.

## 🚀 Features

### Calculator Features
- **Professional UI** with modern glassmorphism design
- **Interactive operations** with visual feedback
- **Real-time calculations** via REST API
- **Responsive design** for mobile and desktop
- **Error handling** with user-friendly messages
- **Keyboard support** (Enter to calculate)

### Technical Features
- **Flask web framework** with REST API
- **Comprehensive testing** with pytest
- **Security hardened** code (fixed all CWE issues)
- **Input validation** against NaN/Infinity attacks
- **Environment-based configuration**

### DevOps Features
- **Jenkins CI/CD pipeline** automation
- **Automated testing** on every commit
- **Local deployment** with environment setup
- **GitHub integration** with webhook support

## 🛠️ Quick Start

### Prerequisites
- Python 3.8+
- Git
- Jenkins (for CI/CD)

### Local Development
```bash
# Clone repository
git clone <your-repo-url>
cd python-jenkins-app

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Start application
python main.py
```

### Access Application
- **Web Interface:** http://127.0.0.1:5000
- **API Endpoint:** POST /calculate

## 🔧 Jenkins Pipeline

The automated pipeline includes:

1. **Checkout** - Pull code from GitHub
2. **Environment Setup** - Create virtual environment
3. **Dependencies** - Install requirements.txt
4. **Testing** - Run pytest with coverage
5. **Security Scan** - Code quality checks
6. **Packaging** - Prepare for deployment
7. **Deploy** - Local deployment with run script

### Pipeline Configuration
- **Trigger:** GitHub webhook on push
- **Environment:** Windows/Linux compatible
- **Security:** Localhost binding, debug disabled
- **Artifacts:** Deploy folder with run script

## 📁 Project Structure
```
python-jenkins-app/
├── main.py              # Flask application
├── requirements.txt     # Dependencies
├── Jenkinsfile         # CI/CD pipeline
├── templates/
│   └── calculator.html # Professional UI
├── tests/
│   ├── __init__.py
│   └── test_app.py     # Unit tests
├── deploy/             # Deployment artifacts
├── .gitignore
└── README.md
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=main

# Test specific function
python -m pytest tests/test_app.py::TestCalculator::test_api_calculate -v
```

## 🔒 Security Features

- ✅ **Input validation** against NaN/Infinity injection
- ✅ **Host binding** restricted to localhost
- ✅ **Debug mode** controlled via environment
- ✅ **Error handling** without information leakage
- ✅ **Dependencies** updated to secure versions
- ✅ **Type safety** with comprehensive validation

## 🚀 Deployment

### Manual Deployment
```bash
# From deploy folder
cd deploy
run.bat  # Windows
# ./run.sh  # Linux (if created)
```

### Jenkins Deployment
Pipeline automatically:
1. Creates `deploy/` folder
2. Copies application files
3. Generates `run.bat` with environment variables
4. Provides access instructions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🔗 Links

- **GitHub Repository:** [Your Repo URL]
- **Jenkins Dashboard:** http://localhost:8080
- **Application:** http://127.0.0.1:5000

---

**Built with ❤️ using Flask, Jenkins, and modern web technologies**
