/*  
Author: Nguyen Mai Hung
Date: 2023-07-26
Verison: 1.4
Project: dev-api-storage
Description: This Jenkinsfile automates the CI/CD process for the project.
*/

pipeline {
    agent any

    
    // Environment
    environment {

        // API Telegram Token
        telegramBotToken = '1481210476:AAGOM-RnZM6zOJ5hNBzffqPKE1YY-n6wGDk'
        chatId = '-832392518'
   
        // Template Telegram message
        header = "\ud83d\udd01 <b>QUY TRÌNH CI/CD v1.1</b>\n\ud83c\udd94 <code>${env.JOB_NAME}</code>"
        separator = "\u2796\u2796\u2796\u2796\u2796\u2796\u2796\u2796\u2796\u2796"
        footer = "\u2139 Chi tiết logs: ${env.BUILD_URL}"

        // Server credentials
        serverIP = '103.168.51.73'
        serverUser = 'root'

        // Code directory and Docker Compose settings
        homeDirectory = '/home/pvs'
        codeDirectory = '/home/pvs/dev-api-storage'
        composeFilePath = '/home/pvs/docker-compose.yml'
        dockerServiceName = 'dev-api-storage-django'

        // Git build branch
        git_branch = 'master'

    }

    // Simple CI/CD Stages
    stages {
        // stage 'Get Latest Git Commit Logs'
        stage('Get Latest Git Commit Logs') {
            steps {
                script {
                    def repositoryLink = sh(returnStdout: true, script: 'git config --get remote.origin.url')
                    env.GIT_repositoryLink = repositoryLink.trim()
                    def commitPerson = sh(returnStdout: true, script: 'git log -1 --pretty=format:"%an"')
                    env.GIT_commitPerson = commitPerson.trim()
                    def commitTime = sh(returnStdout: true, script: 'git log -1 --pretty=format:"%ci"')
                    env.GIT_commitTime = commitTime.trim()
                    def commitMessage = sh(returnStdout: true, script: 'git log -1 --pretty=format:"%s"')
                    env.GIT_commitMessage = commitMessage.trim()
                }
            }
        }

        // stage 'Send Git Logs to Telegram'
        stage('Send Git Logs to Telegram') {
            steps {
                script {

                    def message =   "\ud83c\udd95 Có cập nhật coding mới trên git repository !\n\n" +
                                    "${separator}\n" +
                                    "\ud83c\udd94 <code>${env.JOB_NAME}</code>\n" +
                                    "${separator}\n" +
                                    "\ud83d\udd17 Link: <code>${env.GIT_repositoryLink}</code>\n" +
                                    "\ud83e\uddd1 Người thực hiện: <code>${env.GIT_commitPerson}</code>\n" +
                                    "\ud83d\udcc5 Thời gian: <code>${env.GIT_commitTime}</code>\n" +
                                    "\ud83c\udd95 Nội dung: <code>${env.GIT_commitMessage}</code>\n" +
                                    "${separator}\n" +
                                    "\ud83d\udd01 Cập nhật này sẽ được tự động triển khai và tích hợp bằng quy trình CI/CD."

                    sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\":\"${chatId}\", \"text\":\"${message}\", \"parse_mode\":\"HTML\"}' https://api.telegram.org/bot${telegramBotToken}/sendMessage"
                }
            }
        }    

        // stage 'Login to Server'
        stage('Login to Server') {
            steps {
                echo "Logging into the server..."
                sshagent(credentials: ['KEY_Jenkins_Server']) {
                    sh 'ssh -o StrictHostKeyChecking=no ${serverUser}@${serverIP}'
                }
                echo "Success login"
            }
        }

        // stage: 'Pull code'
        stage('Pull Code') {
            steps {
                sshagent(credentials: ['KEY_Jenkins_Server']) {
                    sh "ssh -o StrictHostKeyChecking=no ${serverUser}@${serverIP} \"cd ${codeDirectory} && git pull origin ${git_branch}\""
                }
                echo "Code pulled successfully"
            }
        }

        // stage: 'Build Code'
        stage('Build Code') {
            steps {
                sshagent(credentials: ['KEY_Jenkins_Server']) {
                    sh "ssh -o StrictHostKeyChecking=no ${serverUser}@${serverIP} \"cd ${homeDirectory} && docker-compose -f ${composeFilePath} up -d --build ${dockerServiceName}\""
                }
                echo "Code build successfully"
            }
        }
    }

    // Notification to Telegram
    post {
        // if success
        success {
            script {
                def status = "\u2705 Trạng thái: Thành công"
                def message = "${header}\n${separator}\n${status}\n${separator}\n${footer}"
                sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\":\"${chatId}\", \"text\":\"${message}\", \"parse_mode\":\"HTML\"}' https://api.telegram.org/bot${telegramBotToken}/sendMessage"
            }
        }
        // if failure
        failure {
            script {
                def status = "\u274c Trạng thái: Thất bại"               
                def message = "${header}\n${separator}\n${status}\n${separator}\n${footer}"               
                sh "curl -X POST -H 'Content-Type: application/json' -d '{\"chat_id\":\"${chatId}\", \"text\":\"${message}\", \"parse_mode\":\"HTML\"}' https://api.telegram.org/bot${telegramBotToken}/sendMessage"   
            }
        }
    }
}
