pipeline {
    agent any

    stages {
        stage('Check Branch Differences') {
            steps {
                script {
                    // def runCommand = { String command ->
                    //     def proc = command.execute()
                    //     proc.waitFor()
                    //     return proc.in.text.trim()
                    // }
                    sh("git checkout dev")

                    echo "[INFO] Fetching latest changes from remote..."
                    echo sh("git fetch origin")

                    def remoteDiff = sh("git log dev..origin/dev --oneline")
                    def localDiff = sh("git log origin/dev..dev --oneline")
                    echo remoteDiff
                    echo localDiff

                    echo "\n[INFO] Commits in remote 'origin/dev' but not in local 'dev':"
                    echo remoteDiff ? remoteDiff : "✅ No new commits in remote."

                    echo "\n[INFO] Commits in local 'dev' but not in remote 'origin/dev':"
                    echo localDiff ? localDiff : "✅ No new commits in local."

                    if (remoteDiff || localDiff) {
                        echo "\n🔁 [RESULT] Local 'dev' and remote 'origin/dev' branches are DIFFERENT."
                        // You can choose to fail the build if desired:
                        // error("Branches are out of sync!")
                    } else {
                        echo "\n✅ [RESULT] Local 'dev' and remote 'origin/dev' branches are IDENTICAL."
                    }
                }
            }
        }
    }
}


// pipeline {
//     agent any

//     environment {
//         BRANCH_NAME = 'main'
//     }

//     stages {
//         stage('Check for New Commits in Main Branch') {
//             steps {
//                 script {
//                     // Fetch the latest changes
//                     sh 'git fetch origin main'

//                     // Get the latest commit on the current branch (main)
//                     def latestCommit = sh(script: "git rev-parse origin/${BRANCH_NAME}", returnStdout: true).trim()
//                     echo "Latest commit on ${BRANCH_NAME}: ${latestCommit}"

//                     // Get the commit from the previous build
//                     def lastCommit = currentBuild.previousBuild?.getEnvironment()?.get("GIT_COMMIT")

//                     if (lastCommit) {
//                         echo "Last build commit: ${lastCommit}"

//                         // Check if there are new commits
//                         if (lastCommit != latestCommit) {
//                             echo "New commits detected in '${BRANCH_NAME}' branch."
//                             def logOutput = sh(script: "git log ${lastCommit}..origin/${BRANCH_NAME} --oneline", returnStdout: true).trim()
//                             echo "New commits since last build:\n${logOutput}"
//                             // Trigger further stages as needed
//                         } else {
//                             echo "No new commits in '${BRANCH_NAME}' since last build."
//                         }
//                     } else {
//                         echo "No previous build commit found. Proceeding with the latest commit."
//                         // Proceed with the latest commit
//                     }
//                 }
//             }
//         }
//     }
// }
