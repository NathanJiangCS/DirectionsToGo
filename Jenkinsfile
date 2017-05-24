node("NathanPC") {
    
     currentBuild.result = "SUCCESS"
     
     try {
         stage("Checkout"){
            checkout scm
         }
         
         stage("Get Docker"){
             sh "export PATH=$PATH:/usr/local/bin"
             sh "env"
             docker.image('python:2.7.13').inside {
                 stage("Test") {
                    sh "pip -V"
                 }
             }
         }
         
         step([$class: 'WsCleanup'])
         
         
     }
     
     catch (err) {
        currentBuild.result = "SUCCESS"
         throw err
     }
     
}
