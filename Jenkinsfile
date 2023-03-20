pipeline {
  agent any
  stages {
    stage('Install python modules') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('copy secrets') {
      steps {
        sh 'cp .env.example .env'
      }
    }
    stage('Data creation') {
      steps {
        sh 'python data_creation.py'
      }
    }
    stage('Model_preprocessing') {
      steps {
        sh 'python model_preprocessing.py'
      }
    }
    stage('Model_preparation') {
      steps {
        sh 'python model_preparation.py'
      }
    }
    stage('Model_testing') {
      steps {
        sh 'python model_testing.py'
      }
    }
  }
}
