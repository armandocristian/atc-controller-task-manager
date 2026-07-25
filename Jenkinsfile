pipeline {

    agent any

    environment {
        IMAGE_NAME = "atc-todo-app"
    }

    stages {

        stage('Checkout') {

            steps {
                echo "Downloading source code"
                checkout scm
            }
        }


        stage('Install Dependencies') {

            steps {

                echo "Installing Python dependencies"

                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''

            }
        }


        stage('Run Tests') {

            steps {

                echo "Running pytest"

                sh '''
                . venv/bin/activate
                pytest
                '''

            }
        }


        stage('Build Docker Image') {

            steps {

                echo "Building Docker image"

                sh '''
                docker build -t ${IMAGE_NAME}:latest .
                '''

            }
        }

    }


    post {

        success {

            echo "ATC Pipeline completed successfully"

        }

        failure {

            echo "ATC Pipeline failed"

        }

    }

}
