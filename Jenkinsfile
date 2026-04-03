pipeline {
    agent any 

    options {
        timestamps()
        timeout(time: 5, unit: 'MINUTES')
        retry(2)
    }

    parameters {
        string(name: 'BROWSER', defaultValue: 'chrome')
        string(name: 'ENV', defaultValue: 'prod')
        string(name: 'TAGS', defaultValue: 'api')
    }

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/nareshkaliamoorthy/PlaywrightAPITest_2x.git',
                        credentialsId: 'knareshtr'
                    ]]
                ])
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Tests') {
            steps {
                bat '''
                    if exist reports\\allure-results rmdir /s /q reports\\allure-results
                    call venv\\Scripts\\activate
                    pytest -m "%TAGS%" --browser "%BROWSER%" --base-url "%ENV%" --alluredir=reports\\allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
        }
        failure {
            echo "Build Failed! Check Allure Report."
        }
    }
}