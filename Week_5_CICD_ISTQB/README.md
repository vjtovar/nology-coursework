# CICD_ISTQB

## Project: Intro to CICD

### Overview
A Javascript app with unit tests connected to Jenkins for CICD

### Specifications
1. Create repo on github
2. Setup Jenkins
3. Setup AWS

### Jenkins Setup (Day 1) 
1. Create repo on github
2. Connect remote repo to local app
```
app echo "# jenkins-lesson" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vjtovar/jenkins-lesson.git
git push -u origin main
```
3. ```git status``` to check files that need to be pushed
4. Push files that are still on local app
5. Make directory in root ```mkdir .ssh```
6. Go into directory ```cd .ssh```
7. Generating public/private rsa key pair for Jenkins ```ssh-keygen -t rsa```
8.  Enter file in which to save the key (/Users/vjtovar/.ssh/id_rsa): ```JenkinsKey```
9. Don't enter passphrase
10. The files JenkinsKey and JenkinsKey.pub should be in the directory
11. The private key is in the file without the .pub. To open the SSH private key ```cat JenkinsKey```
12. Copy everything below and paste into Jenkins credentials. Make sure not to copy any spaces
```
-----BEGIN OPENSSH PRIVATE KEY-----

-----END OPENSSH PRIVATE KEY-----
```
13. Create Jenkins account
14. Click on new item, enter item name VALERIE-TOVAR-CI, click freestyle project, click ok
15. In General section; GitHub project url: enter SSH repo, restrict where project can be run: NodeJS, source code management: click git and paste github SSH repo, credentials: type Jenkins, click Jenkins, click ok
16. Jenkins credential provider will popup, domain: global credentials(unrestricted) kind: SSH username with private key, scope: Global (Jenkins, nodes, items, all child items, etc), ID: VT-JK, description: Key Pair to Acess GH-VT, username: VT, copy and paste Jenkins private key into text box and click ok, from credentials dropdown select your key: VT-JK (Key Pair to Acess GH-VT), then save. Will see error message: Failed to connect to repository : Error performing git command: git ls-remote -h git@github.com:vjtovar/ASML_NologyBot_Team2.git HEAD. It is ok for now.

### Jenkins Setup (Day 2) 
1. Go into app repo settings, click on deploy key, click on add new.
2. For the Title enter: jenkinskey, copy and paste JenkinsKey.pub public key into github repo. Allow write access(must be checked), click add key. It must say never used-Read/write
3. Go to Jenkins website, go to project, go to configure, go to branches to build, go to branch specifier: change it to main, click save
4. In Jenkins test the connection, go to build now, at the bottom looks like connecting. The green check means successful, click on the #1, then go to console output to check if successful.
5. In Jenkins go back to project, go to configure, go to build, add build step, click execute shell, type in location of folder(if several folders in make sure to add it (ex: cd app/app). Because packages are not stored on github need to install them (ex: npm install). Then need to run the json script(ex: npm run test). Then click save
```cd app```
```npm install```
```npm run test```
6. In Jenkins test the connection, go to build now, at the bottom looks like connecting. Click on the #2, check the console output, make sure there are no errors.
7. To setup webhooks to trigger something to happen go to the github repo, go to settings, go to webhooks, click add webhooks, payload url is the jenkins website url with the 8080 then add /github-webhook/ to the end of it (ex: http://#.###.###.###:8080/github-webhook/). Make sure "just the push event" and "active" are both checked, then click add webhook.
8. Go to the Jenkins website, go to configure, scroll down to build triggers, click on GitHub hook trigger for GITScm polling?
9. Go to the app on vs code, make a change like add a comment in index.js, then push to github.
10. In the repo github webhooks make sure there is a green check mark next to the webhook. In Jenkins should see a green check mark for the #3 build, then when go to console output it should say github push by vjtovar.
11. This is just for extra info: In Jenkins go back to the project, got to configure, go to build, scroll to post-build actions from the drop down select git publisher, select push only if build succeeds and merge results, in branches to push to remote repo click add branch, in branch to push add main, in target remote name add origin, then add branch name (ex: */feature-branch). Go to app in vscode, checkout a branch with the same name, make a change and push branch to github. This will merge the branch into main automatically.

### AWS Setup
A server is a computer without a GUI
1. Follow this link https://########3907.signin.aws.amazon.com/console to login into AWS
2. EC2 = elastic compute, setup server. Go to servers, compute, EC2
3. Click launch instance, enter name: ASML-ValerieTovar-EC2, OS System: Ubuntu Server 18.04 LTS (HVM) SSD Volume Type, Instance Type: t2.micro, 
4. To create SSH key go to key pair(login), click create new key pair, enter name: ValerieTovar_ASML_Key, make sure RSA is clicked and file format: .pem is clicked, click create key pair. It should select the key
5. vpc = virtual private cloud (version of local network). In Network settings: click edit, from VPC dropdown pick vpc-##### (nology-training-usa), subnet: subnet-##### nology-training-usa-ansible-private, auto-assign public IP: enable, check off select existing security group, from drop down select Dallas Training Group - SSH Access sg-#####, number of instances: 1, click launch instance(should be green if server created)
6. Move downloaded private key to ~/.ssh folder. In downloads: ```mv ./ValerieTovar-ASML-Key.pem ~/.ssh/```
7. In .ssh folder have to change permissions of file, setting it to 400 changes it to read only: ```chmod 400 ValerieTovar-ASML-Key.pem```
8. Then copy the auto-assigned public IP address from AWS and paste it in the command: ```ssh -i ValerieTovar-ASML-Key.pem ubuntu@#.###.###.#```
9. Should see that it succesfully connected to the server. To exit: ```exit```
10. To set up config file in .ssh folder: ```nano config```
11. Then in config add: 
```
Host IPTOCONNETCTO 
IdentityFile ROUTETOPEMFILE           
IdentitiesOnly yes
```
12. To save the changes type control o, then type enter, to exit type control x
13. Then when want to connect to the server only have to enter in the terminal ```ssh ubuntu@#.###.###.#```
14. To turn off the connection in AWS, go into instance, check off your server, click instance state, then click stop instance.

