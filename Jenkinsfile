pipeline {
    agent any

    stages {
        stage('Check Branch Differences') {
            steps {
                script {
                   
                    sh("git checkout dev")

                    echo "[INFO] Fetching latest changes from remote..."
                    echo sh("git fetch origin")

                    def remoteDiff = sh(script: "git log dev..origin/dev --oneline", returnStdout: true).trim()
                    def localDiff = sh(script: "git log origin/dev..dev --oneline", returnStdout: true).trim()

                    echo "remoteDiff: ${remoteDiff}"
                    echo "localDiff: ${localDiff}"

                    echo "\n[INFO] Commits in remote 'origin/dev' but not in local 'dev':"
                    echo remoteDiff ? remoteDiff : "✅ No new commits in remote."

                    echo "\n[INFO] Commits in local 'dev' but not in remote 'origin/dev':"
                    echo localDiff ? localDiff : "✅ No new commits in local."

                    if (remoteDiff || localDiff) {
                       
                        // Get changed files and extract folder paths
                        def changedFiles = sh(script: "git diff --name-only origin/dev..dev", returnStdout: true).trim()
                        if (changedFiles) {
                            def folders = changedFiles
                                .split('\n')
                                .findAll { it.contains('/') } // Exclude root-level files
                                .collect { it.tokenize('/')[0] }
                                .unique()

                            if (folders) {
                                echo "\n✅ [RESULT] New commits have been detected."
                                sh("git pull")
                                for (int i = 0; i < folders.size(); i++) {
                                    echo "${folders[i]}"
                                }
        
                            }else {
                                 echo "\n ✅ [RESULT] New commits have been detected ❌ but no need for modules update"
                                 sh("git pull")
                            }
                        }
                        
                    } else {
                        echo "\n❌ [RESULT] No new commits detected."
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
