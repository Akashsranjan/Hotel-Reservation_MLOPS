pipeline {
    agent any

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps {
                echo 'Cloning Github repo to Jenkins............'

               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token1', url: 'https://github.com/Akashsranjan/Hotel-Reservation_MLOPS.git']])
            }
        }
    }
}
