# Pipeline with Jenkins
In Development mode.

1. Install Jenkins by [instruction](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-20-04):

2. Create new pipeline:

  2.1. Add new item:
  ![pipeline step 1](./assets/jenkins/setup_pipeline_01.png)

  2.2. Fill field 'Item name', select 'multibranch pipeline' and press ok:
  ![pipeline step 2](./assets/jenkins/setup_pipeline_02.png)

  2.3. Fill 'Display Name', 'Description' fields and press 'Add source' in 'Branch Sources block':
  ![pipeline step 3](./assets/jenkins/setup_pipeline_03.png)

  2.4. Select type 'GitHub' and fill username of your github account and fill 'Password' field with personal access token, created only for access jenkins to this repo:
  ![pipeline step 4](./assets/jenkins/setup_pipeline_04.png)
  Press button 'Add' and select type of branches, used in pipeline:

  ![pipeline step 5](./assets/jenkins/setup_pipeline_05.png)

  2.5. Press 'Save' button in bottom of page. All is ready:

3. Visit dashboard page: [http://0.0.0.0:8080](http://0.0.0.0:8080)
You'll see created pipeline, named 'smlp':
![dashboard](./assets/jenkins/pipeline01.png)

4. Visit pipeline page (click on it link):
![pipeline](./assets/jenkins/pipeline02.png)

5. See the stages:
![stages](./assets/jenkins/pipeline03.png)

6. All stages placed in [Jenkinsfile](../Jenkinsfile) in root of repository.

7. To see the logs, press here:
![logs1](./assets/jenkins/logs01.png)
and press 'Console output':
![logs2](./assets/jenkins/logs02.png)
You would see logs of each stage:
![logs3](./assets/jenkins/logs03.png)
![logs4](./assets/jenkins/logs04.png)
![logs5](./assets/jenkins/logs05.png)
