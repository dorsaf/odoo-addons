pipeline {
    agent any

    environment {
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Check for New Commits in Main Branch') {
            steps {
                script {
                    // Fetch the latest changes
                    sh 'git fetch origin main'

                    // Get the latest commit on the current branch (main)
                    def latestCommit = sh(script: "git rev-parse origin/${BRANCH_NAME}", returnStdout: true).trim()
                    echo "Latest commit on ${BRANCH_NAME}: ${latestCommit}"

                    // Get the commit from the previous build
                    def lastCommit = currentBuild.previousBuild?.getEnvironment()?.get("GIT_COMMIT")

                    if (lastCommit) {
                        echo "Last build commit: ${lastCommit}"

                        // Check if there are new commits
                        if (lastCommit != latestCommit) {
                            echo "New commits detected in '${BRANCH_NAME}' branch."
                            def logOutput = sh(script: "git log ${lastCommit}..origin/${BRANCH_NAME} --oneline", returnStdout: true).trim()
                            echo "New commits since last build:\n${logOutput}"
                            // Trigger further stages as needed
                        } else {
                            echo "No new commits in '${BRANCH_NAME}' since last build."
                        }
                    } else {
                        echo "No previous build commit found. Proceeding with the latest commit."
                        // Proceed with the latest commit
                    }
                }
            }
        }
    }
}
