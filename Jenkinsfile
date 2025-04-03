pipeline {
    agent any

    environment {
        AZURE_APP_NAME = "your-azure-app-name"
        AZURE_RESOURCE_GROUP = "your-resource-group"
        AZURE_SUBSCRIPTION_ID = "your-subscription-id"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/naitikjain25/python-azure-app.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && pip install --upgrade pip'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate && pytest' // If you have tests
            }
        }

        stage('Deploy to Azure') {
            steps {
                bat 'az login --service-principal -u "your-client-id" -p "your-client-secret" --tenant "your-tenant-id"'
                bat 'az webapp up --name %AZURE_APP_NAME% --resource-group %AZURE_RESOURCE_GROUP% --runtime "PYTHON:3.10"'
            }
        }
    }

    post {
        failure {
            echo 'Deployment Failed!'
        }
        success {
            echo 'Deployment Successful!'
        }
    }
}
