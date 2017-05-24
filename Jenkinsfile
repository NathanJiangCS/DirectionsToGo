node("NathanPC") {
    
     currentBuild.result = "SUCCESS"
     
     try {
         stage("Checkout"){
            checkout scm
         }
         
         stage("Get Docker"){
             sh "cat /tmp/Jenkins/workspace/python2-docker@tmp/*/script.sh"
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
