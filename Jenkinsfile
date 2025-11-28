// groovylint-disable CompileStatic, NoDef
pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')  // 每5分钟检查一次
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:lxl608608/auto_api_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    cd auto_api_test
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    cd auto_api_test
                    pytest script/ -v -s --html=report/html_report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'auto_api_test/report',
                reportFiles: 'html_report.html',
                reportName: 'HTML Report'
            ]
        }
    }
}
