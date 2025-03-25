pipeline {
    agent any
    
    environment {
        GIT_URL = 'git@github.com:dorsaf/odoo-addons.git'
        BRANCH = 'main'
        TARGET_FOLDER = 'module_2/' // Specify the folder to monitor
    }
    
    stages {
        
        stage('Check for Changes') {
            steps {
                script {
                    def changes = sh(script: "git diff --name-only HEAD~1 HEAD | grep ^${TARGET_FOLDER} || true", returnStdout: true).trim()
                    
                    if (changes) {
                        echo "Changes detected in ${TARGET_FOLDER}"
                        env.CHANGES_DETECTED = 'true'
                    } else {
                        echo "No changes detected in ${TARGET_FOLDER}. Skipping further stages."
                        env.CHANGES_DETECTED = 'false'
                    }
                }
            }
        }
        
        stage('Pull Latest Changes') {
            when {
                expression { env.CHANGES_DETECTED == 'true' }
            }
            steps {
                script {
                    sh 'git pull origin ${BRANCH}'
                }
            }
        }
        
        stage('Build & Deploy') {
            when {
                expression { env.CHANGES_DETECTED == 'true' }
            }
            steps {
                echo 'Building and deploying the project...'
                // Add build/deploy steps here
            }
        }
    }
}
