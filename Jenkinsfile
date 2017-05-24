node("master") {
    
     currentBuild.result = "SUCCESS"
     
     try {
         stage("Checkout"){
            checkout scm
         }
         
         stage("Get Docker"){
             docker.image('python:2.7.13') {
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
