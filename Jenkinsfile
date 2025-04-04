pipeline {
    agent any

    environment {
        AZURE_CREDENTIALS_ID = 'azure-service-principal'
        RESOURCE_GROUP = 'rg-jenkins'
        APP_SERVICE_NAME = 'webapijenkinsnaitik457'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/naitikjain25/python-azure-app.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                bat '"C:\\Users\\NAITIK JAIN\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
                bat '.\\venv\\Scripts\\activate && .\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.\\venv\\Scripts\\activate && .\\venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.\\venv\\Scripts\\activate && .\\venv\\Scripts\\python.exe -m pip install pytest' // Ensure pytest is installed
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate && .\\venv\\Scripts\\python.exe -m pytest' // Run tests properly
            }
        }

        // stage('Deploy to Azure') {
        //     steps {
        //         bat 'az login --service-principal -u "your-client-id" -p "your-client-secret" --tenant "your-tenant-id"'
        //         bat 'az webapp up --name %AZURE_APP_NAME% --resource-group %AZURE_RESOURCE_GROUP% --runtime "PYTHON|3.12"'
        //     }
        // }
        stage('Deploy') {
            steps {
                withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                    bat "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"
                    bat "powershell Compress-Archive -Path ./publish/* -DestinationPath ./publish.zip -Force"
                    bat "az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_SERVICE_NAME --src-path ./publish.zip --type zip"
                }
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
