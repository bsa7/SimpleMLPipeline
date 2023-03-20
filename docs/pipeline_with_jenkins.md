# Pipeline with Jenkins
In Development mode.

1. Run Jenkins in docker:
```bash
docker-compose up
```

At first run you not need to daemonize docker-compose, because jenkins show you temporary pasword:
```bash
jenkins_1  |
jenkins_1  | Jenkins initial setup is required. An admin user has been created and a password generated.
jenkins_1  | Please use the following password to proceed to installation:
jenkins_1  |
jenkins_1  | 173ef2c01d75408482e1b72478af2073
jenkins_1  |
jenkins_1  | This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
jenkins_1  |
jenkins_1  | *************************************************************
jenkins_1  | *************************************************************
jenkins_1  | *************************************************************
```

Copy that password to clipboard.

2. Open Jenkins in brovser. Visit address [http://0.0.0.0:8080/](http://0.0.0.0:8080/), you must see initialization screen:

![Jenkins first screen](./assets/jenkins/first_screen.png)
Paste password in 'Administrator password' field and press 'Continue'.

3. Press button "Install suggested plugins" as shown here:
![Jenkins plugin installation page](./assets/jenkins/plugins_installation_page.png)

4. Be patience, wait while all plugins are installed:
![Jenkins plugin installation process](./assets/jenkins/plugins_installation_page2.png)

5. For working with repo, create your personal access token:

    5.1. Visit [https://github.com/settings/tokens](https://github.com/settings/tokens) and press 'Generate new token (classic)' as shown below:

    ![Generate personal access token](./assets/jenkins/generate_personal_access_token.png)

    5.2. Check 'repo' checkbox and enter name of token as show on image:

    ![Generate personal access token 2](./assets/jenkins/generate_personal_access_token2.png)

    5.3. Press green button 'Generate token' at bottom of page.

    5.4. Copy secret token to clipboard:

    ![Generate personal access token 3](./assets/jenkins/generate_personal_access_token3.png)

6. Return to Jenkins [http://0.0.0.0:8080/](http://0.0.0.0:8080/) and fill the form:
  ![Setup admin](./assets/jenkins/jenkins_setup_admin.png)

  Follow next page without changes. Press bottom right button and button "Start using Jenkins" in final:

  ![jenkins setup finished](./assets/jenkins/jenkins_setup_finished.png)

7. Create new pipeline:

  7.1. Add new item:
  ![pipeline step 1](./assets/jenkins/setup_pipeline_01.png)

  7.2. Fill field 'Item name', select 'multibranch pipeline' and press ok:
  ![pipeline step 2](./assets/jenkins/setup_pipeline_02.png)

  7.3. Fill 'Display Name', 'Description' fields and press 'Add source' in 'Branch Sources block':
  ![pipeline step 3](./assets/jenkins/setup_pipeline_03.png)

  7.4. Select type 'GitHub' and fill username of your github account and fill 'Password' field with token, copied on step 5.4.:
  ![pipeline step 4](./assets/jenkins/setup_pipeline_04.png)
  Press button 'Add' and select type of branches, used in pipeline:

  ![pipeline step 5](./assets/jenkins/setup_pipeline_05.png)

  7.5. Press 'Add' button in bottom of page. All is ready:

8. Visit dashboard page: [http://0.0.0.0:8080](http://0.0.0.0:8080)
You'll see created pipeline, named 'smlp':
![dashboard](./assets/jenkins/pipeline01.png)

9. Visit pipeline page (click on it link):
![pipeline](./assets/jenkins/pipeline02.png)

10. See the stages:
![stages](./assets/jenkins/pipeline03.png)

11. All stages placed in [Jenkinsfile](../Jenkinsfile) in root of repository.

12. To see the logs, press here:
![logs1](./assets/jenkins/logs01.png)
and press 'Console output':
![logs2](./assets/jenkins/logs02.png)
You would see logs of each stage:
![logs3](./assets/jenkins/logs03.png)
![logs4](./assets/jenkins/logs04.png)
![logs5](./assets/jenkins/logs05.png)
