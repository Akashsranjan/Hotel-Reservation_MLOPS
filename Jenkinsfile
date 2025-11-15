pipeline {
    agent any

    environment {
        VENV_DIR = 'mlops'
        GCP_PROJECT = 'mlops-474603'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {

        stage('Cloning GitHub Repo') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token1',
                            url: 'https://github.com/Akashsranjan/Hotel-Reservation_MLOPS.git'
                        ]]
                    )
                }
            }
        }

        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                script {
                    echo 'Creating virtual env and installing dependencies...'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Build & Push Docker Image to GCR') {
            steps {
                echo 'Building Docker Image and pushing to GCR...'
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {

                    script {
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "Activating Google Cloud Service Account..."
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        echo "Setting GCP project..."
                        gcloud config set project ${GCP_PROJECT}

                        echo "Configuring Docker to use GCR..."
                        gcloud auth configure-docker --quiet

                        echo "Building Docker image..."
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        echo "Pushing Docker image to GCR..."
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
    }
}
