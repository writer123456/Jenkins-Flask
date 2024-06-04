pipeline {
    agent any

    triggers {
        githubPush()
    }
    environment{
        // AWS_ACCESS_KEY_ID=credentials('i-05ec74df442215c90')
        GITHUB_URL='https://github.com/writer123456/Jenkins-Flask.git'
        GITHUB_BRANCH='main'
        REGION = 'us-east-1'
        VENV_DIR = '.venv'  // Directory for the virtual environment
        STAGING_DIR = 'C:/Users/USER/' // Path to your staging environment
        
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('Checkout'){
            steps{
                script{
                    git branch: env.GITHUB_BRANCH, url: env.GITHUB_URL
                }
                
                
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Install Python and create a virtual environment
                bat 'C:/Users/USER/AppData/Local/Programs/Python/Python311/python.exe -m venv ${VENV_DIR}'
                bat '${VENV_DIR}\\Scripts\\activate'
                // bat 'source ${VENV_DIR}/bin/activate'
            }
        }
        
        stage('Install dependencies'){
            steps{
                script{
                    bat 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                    bat 'C:/Users/USER/AppData/Local/Programs/Python/Python311/python.exe get-pip.py'
                    bat 'C:/Users/USER/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install flask'
                    bat 'C:/Users/USER/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install pytest'
                }
                
                
            }
        }
        
         stage('Install Dependencies new') {
            steps {
                // Install project dependencies
                bat '''
                C:/Users/USER/AppData/Local/Programs/Python/Python311/Scripts/pip.exe install --upgrade pip
                '''
            }
        }
        
        stage('Start Flask Application') {
            steps {
                // Start the Flask application in the background
                bat '${VENV_DIR}\\Scripts\\activate'
                bat  'start /b python app.py'
                // Wait for a few seconds to ensure the Flask app starts
               powershell 'Start-Sleep -Seconds 5'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Activate virtual environment and run pytest
               bat '${VENV_DIR}\\Scripts\\activate'
               bat 'start /b python test_app.py'
               
               script {
                    // Check the result of the pytest execution
                    def pytestExitCode = bat returnStatus: true, script: "python test_app.py"
                    if (pytestExitCode == 0) {
                        echo 'Tests passed! Proceeding to deploy...'
                        bat '${VENV_DIR}\\Scripts\\activate'
                        bat """
                            echo Deploying to staging environment...
                            REM Copy files to staging server
                            """
                           
                        // bat 'robocopy . ${STAGING_DIR} /E /XD ${STAGING_DIR}'
                        bat 'cd ${STAGING_DIR}'
                        bat 'git clone ${GITHUB_URL}'
                        bat 'echo Deployment complete.'
                            
                       
                    } else {
                        echo 'Tests failed. Aborting deployment.'
                        
                    }
                }

               
              
            }
            
        }
        
        
        
     }
    
}
