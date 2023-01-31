# Flask_MongoDB

## Project: MongoDB

### Overview
Unit Testing using TDD before creating a Flask app with and API generated using MongoDB 

### Specifications
1. Install python
2. Set up virtual environment
3. Install pyenv
4. Install flask
5. Install pytest
6. Use pytest for TDD unit testing 
7. Once tests pass create database and create queries

### Python Installation 
1. Python3 - Download the latest version of python from the python site. run: ```brew install python3```. This should also install pip3. To check Python version, run: ```python3 --version```.
2. pip3 - To check if pip3 is already installed, run: ```pip3 --version```. The output should
be similar to pip 22.2.1.

### Virtual Environment Installation
1. Install virtual env package: ```pip3 install virtualenv```. Only needs to be done once, when first installing python.
2. Make directory for env: ```mkdir flask-api && cd flask-api```
3. Create environment: ```python3 -m venv env```
4. Activate environment: ```source env/bin/activate```. (env) indicates environment is active. 
5. run: ```brew install pyenv```. Only needs to be installed once. Check the version of pyenv, run: ```pyenv --version```.
6. If pyenv version not 3.10.7, run: ```pyenv install 3.10.7```
7. Change the local version to 3.10.7, run: ```pyenv local 3.10.7```
8. run: ```pyenv local``` to check the version of pyenv

### Flask Installation
1. Install flask, run: ```pip3 install flask```
2. Create app.py and add imports
3. run: ```export FLASK_APP=app.py```
4. run: ```flask --debug run```, to start the server
5. Create requirements.txt file and add flask, python-dotenv, psycopg2 to top of file
6. run: ```pip3 install -r requirements.txt```, to install flask, python-dotenv, psycopg2
7. run: ```flask --debug run``` or add FLASK_APP=app, FLASK_DEBUG=1 to .env file to automatically have debugger on. This starts the server

### MongoDB Website Setup
1. Signup for MongoDB: mongodb.com
2. Create a new project with a unique name. In database deployments add your IP address.
3. Create a Shared DB cluster, choose the cloud provider AWS, the closest region, and add name of the cluster. Click create cluster.
4. To authenticate connection add username and password. Ensure these credentials are different to your MongoDB Cloud username and password. Save password in application for connection string. Click create user. 
5. Go to the project in MongoDB, click connect, click on connect your application. Select the driver and version. We are using python v3.6 or later for this app.
6. Add your connection string into your application code(mongopass.py). Replace the <password> with the username password.
7. Go to your project in MongoDB and click on browse connections, click on add your own data. Add a database name and collection name. Click on insert document to add data. Use the database name in db client and the collection name in the collection db in app.py

### MongoDB Installation
1. Install MongoDB tools using homebrew, run: ```brew tap mongodb/brew```
2. Update homebrew, run: ```brew update```
3. To install MongoDB, run: ```brew install mongodb-community@6.0```. It includes the mongod server, mongos shared cluster query router, and mongosh the MongoDB shell.
4. To run MongoDB server, run: ```brew services start mongodb-community@6.0```
5. To verify that MongoDB is running, run: ```brew services list```
6. To begin using MongoDB, connect mongosh to the running instance, run: ```mongosh```
7. To install pymongo, run: ```pip3 install pymongo```
8. If there is a SSL: certificate verify failed error, run: ```pip3 install certifi\n/Applications/Python\ 3.10/Install\ Certificates.command``` or in the applications folder open the python app and click on the install certificate file, it should automatically install. 
9. To stop a mongod running as a macOS service, run: ```brew services stop mongodb-community@6.0```

