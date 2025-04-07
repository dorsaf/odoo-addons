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

                    // Get the last build's commit (if any)
                    def lastCommit = ''
                    if (currentBuild.previousBuild) {
                        lastCommit = currentBuild.previousBuild.rawBuild.getEnvironment(listener).get("GIT_COMMIT")
                        echo "Last build commit: ${lastCommit}"
                    } else {
                        echo "No previous build found."
                    }

                    // Get the latest commit on origin/main
                    def latestCommit = sh(script: "git rev-parse origin/${BRANCH_NAME}", returnStdout: true).trim()
                    echo "Latest commit on ${BRANCH_NAME}: ${latestCommit}"

                    if (lastCommit && lastCommit != latestCommit) {
                        echo "New commits detected in '${BRANCH_NAME}' branch."
                        def logOutput = sh(script: "git log ${lastCommit}..origin/${BRANCH_NAME} --oneline", returnStdout: true).trim()
                        echo "New commits since last build:\n${logOutput}"
                        // You can trigger the next stages here
                    } else if (!lastCommit) {
                        echo "Can't determine last commit. Proceeding anyway."
                    } else {
                        echo "No new commits in '${BRANCH_NAME}' since last build."
                        // You can skip further stages if needed
                    }
                }
            }
        }
    }
}
