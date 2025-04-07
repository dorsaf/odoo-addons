pipeline {
    agent any

    environment {
        GIT_URL = 'git@github.com:dorsaf/odoo-addons.git'
        BRANCH = 'main'
    }

    stages {

        stage('Prepare Repo') {
            steps {
                script {
                    // Ensure we're in the correct branch
                    sh """
                        git reset --hard
                        git clean -fd
                        git checkout ${BRANCH}
                        git pull origin ${BRANCH}
                    """
                }
            }
        }

        stage('Check for Changes') {
            steps {
                script {
                    // Get the last two commits
                    def prevCommit = sh(script: "git rev-parse HEAD~1", returnStdout: true).trim()
                    def currCommit = sh(script: "git rev-parse HEAD", returnStdout: true).trim()

                    echo "Comparing commits: ${prevCommit} -> ${currCommit}"

                    def changedFiles = sh(
                        script: "git diff --name-only ${prevCommit} ${currCommit}",
                        returnStdout: true
                    ).trim()

                    if (changedFiles) {
                        echo "Changes detected:"
                        def folderList = changedFiles
                            .split("\n")
                            .collect { it.split("/")[0] } // Top-level folders
                            .unique()
                            .join("\n- ")

                        echo "Folders with changes:\n- ${folderList}"
                        env.CHANGES_DETECTED = 'true'
                    } else {
                        echo "No new changes in the branch."
                        env.CHANGES_DETECTED = 'false'
                    }
                }
            }
        }

        stage('Build & Deploy') {
            when {
                expression { env.CHANGES_DETECTED == 'true' }
            }
            steps {
                echo 'Building and deploying the project...'
                // Add your build and deployment steps here
            }
        }
    }
}
