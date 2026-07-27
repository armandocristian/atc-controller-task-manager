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

		mkdir -p instance

		export DATABASE_PATH=$(pwd)/instance/test.db

                pytest
                '''

            }
        }


        stage('Build Docker Image') {

            steps {

                echo "Building Docker image"

                sh '''
                docker build -t armandopopa/atc-todo-app:1.0 .
                '''

            }
        }


	stage('Push Docker Image') {

    	    steps {

        	echo "Pushing image to Docker Hub"

        	withCredentials([
            	    usernamePassword(
                	credentialsId: 'dockerhub-creds',
                	usernameVariable: 'DOCKER_USER',
                	passwordVariable: 'DOCKER_PASS'
            	    )
                ]) {

            	   sh '''
                   echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

                   docker push armandopopa/atc-todo-app:1.0
                   '''
                }
            }
        }


	stage('Deploy to Kubernetes') {

    	     steps {

		echo "Deploying application to Kubernetes"
        	
		sh '''
		 kubectl apply -f k8s/namespace.yaml
        	kubectl apply -f k8s/deployment.yaml
        	kubectl apply -f k8s/service.yaml        	

		kubectl rollout restart deployment/atc-todo-app -n atc
        	kubectl rollout status deployment/atc-todo-app -n atc
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
