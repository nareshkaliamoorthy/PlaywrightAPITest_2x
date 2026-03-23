pipeline {
    agent any 

    parameters {
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser to run tests on')
        string(name: 'ENV', defaultValue: 'prod', description: 'Target environment')
        string(name: 'TAGS', defaultValue: 'api', description: 'Pytest markers to run (e.g., smoke, regression)')
    }

    tools {
        // Ensure this Name matches what you set in Manage Jenkins -> Tools
        allure 'allure-latest'
    }

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                    credentialsId: 'knareshtr', 
                    url: 'https://github.com/nareshkaliamoorthy/PlaywrightAPITest_2x.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Tests') {
            steps {
                // We use 'exit 0' to ensure the pipeline continues to the Allure report even if tests fail
                bat '''
                    call venv\\Scripts\\activate
                    pytest -m "%TAGS%" --browser "%BROWSER%" --base-url "%ENV%" --alluredir=reports\\allure-results || exit 0
                '''
            }
        }
    }

    post {
        always {
            script {
                // Note: Jenkins Allure plugin handles the path mapping automatically
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
            }
        }
        
        failure {
            echo "Build Failed! Check the Allure Report for screenshots and logs."
        }
    }
}