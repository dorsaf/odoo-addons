pipeline {
    agent any
    
    environment {
        GIT_URL = 'git@github.com:dorsaf/odoo-addons.git'
        BRANCH = 'main'
        TARGET_FOLDER = 'module_2/' // Specify the folder to monitor
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        
        stage('Check for Changes') {
            steps {
                script {
                    def changes = sh(script: "git diff --name-only HEAD~1 HEAD | grep ^${TARGET_FOLDER}", returnStdout: true).trim()
                    
                    if (changes) {
                        echo "Changes detected in ${TARGET_FOLDER}"
                    } else {
                        echo "No changes detected in ${TARGET_FOLDER}. Stopping pipeline."
                        currentBuild.result = 'SUCCESS'
                        error('No changes detected. Skipping further steps.')
                    }
                }
            }
        }
        
        stage('Pull Latest Changes') {
            steps {
                script {
                    sh 'git pull origin ${BRANCH}'
                }
            }
        }
        
        stage('Build & Deploy') {
            steps {
                echo 'Building and deploying the project...'
                // Add build/deploy steps here
            }
        }
    }
}
