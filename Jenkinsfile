pipeline {
  agent any

  parameters {
    choice(
      name: 'BROWSER',
      choices: ['chrome', 'edge', 'firefox', 'safari'],
      description: 'Browser used for the Cucumber scenarios.'
    )
    booleanParam(
      name: 'HEADLESS',
      defaultValue: false,
      description: 'Run Chrome, Edge, or Firefox without a visible window. Safari does not support this.'
    )
  }

  environment {
    JAVA_HOME = '/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home'
    PATH = "/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/3.4.0/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:${env.PATH}"
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'ruby --version'
        sh 'bundle --version'
        sh 'bundle config set --local path vendor/bundle'
        sh 'bundle install --jobs 4 --retry 3'
      }
    }

    stage('Run Cucumber tests') {
      steps {
        withEnv(["BROWSER=${params.BROWSER}", "HEADLESS=${params.HEADLESS}"]) {
          sh 'bundle exec cucumber --profile reports'
        }
      }
      post {
        always {
          publishHTML(target: [
            allowMissing: true,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'reports/cucumber',
            reportFiles: 'cucumber.html',
            reportName: 'Cucumber Report'
          ])
          allure includeProperties: false,
                 jdk: '',
                 results: [[path: 'reports/allure-results']]
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts(
        artifacts: 'reports/cucumber/**, reports/allure-results/**, reports/screenshots/**',
        allowEmptyArchive: true,
        fingerprint: true
      )
    }
  }
}
