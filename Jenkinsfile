pipeline {
    agent any
    
    environment {
        PYTHON_PATH = 'python'
        FLASK_DEBUG = 'false'
        FLASK_HOST = '127.0.0.1'
        FLASK_PORT = '5000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Code already available in workspace...'
                echo 'Skipping SCM checkout for Pipeline script mode'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    python -m pytest tests/ -v --tb=short
                '''
            }
            post {
                always {
                    echo 'Test stage completed'
                }
            }
        }
        
        stage('Package Application') {
            steps {
                echo 'Packaging application...'
                bat '''
                    call venv\\Scripts\\activate.bat
                    echo Build complete - Application ready for deployment
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying Flask application...'
                bat '''
                    if not exist "deploy" mkdir deploy
                    if not exist "deploy\\templates" mkdir deploy\\templates
                    copy main.py deploy\\
                    copy requirements.txt deploy\\
                    copy templates\\calculator.html deploy\\templates\\
                    echo set FLASK_DEBUG=false > deploy\\run.bat
                    echo set FLASK_HOST=127.0.0.1 >> deploy\\run.bat
                    echo set FLASK_PORT=5000 >> deploy\\run.bat
                    echo python main.py >> deploy\\run.bat
                    echo Flask application deployed to local deploy folder
                    echo Run with: cd deploy ^&^& run.bat
                    echo Access at: http://127.0.0.1:5000
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
