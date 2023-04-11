pipeline {
  agent any
  stages {
    stage('Install python modules') {
      steps {
        sh './docker/run "pip install -r requirements.txt"'
      }
    }
    stage('Copy secrets') {
      steps {
        sh 'cp .env.example .env'
      }
    }
    stage('Data creation') {
      steps {
        sh './docker/run "python -m tasks.data_creation"'
      }
    }
    stage('Model preprocessing') {
      steps {
        sh './docker/run "python -m tasks.model_preprocessing"'
      }
    }
    stage('Model preparation') {
      steps {
        sh './docker/run "python -m tasks.model_preparation"'
      }
    }
    stage('Model testing') {
      steps {
        sh './docker/run "python -m tasks.model_testing"'
      }
    }
    stage('Build production Docker image') {
      steps {
        sh 'docker build . -f ./stages/production/Dockerfile.app -t sergiobelevskij/simple-ml-pipeline:$(git tag -l | head)'
      }
    }
    stage('Push production image to Dockerhub') {
      steps {
        sh 'docker push sergiobelevskij/simple-ml-pipeline:$(git tag -l | head)'
      }
    }
  }
}
