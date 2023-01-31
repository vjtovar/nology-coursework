# TDD_Flask_MongoDB

## Project: Flask & MongoDB

### Overview
Unit Testing using TDD before creating a Flask app with an API generated using MongoDB to connect to a machinery parts inventory database and pull in the data.

### Specifications
1. Install python
2. Set up virtual environment
3. Install pyenv
4. Install flask
5. Install pytest
6. Use pytest for TDD unit testing 
7. Once tests pass create database

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

#### Pytest Installation
1. Install pytest, run: ```pip3 install pytest-mongodb```
2. Create requirements.txt file and add requirements
3. run: ```pip3 install -r requirements.txt```, to install requirements
4. run: ```pytest -v -s```, to run tests on application
5. Add pytest-html to requirements.txt file
6. run: ```pip3 install pytest-html```, to install pytest-html
7. run: ```pytest --html=report.html```, this will add report.html file. Open live server to see report of tests
8. run: ```coverage run --omit 'env/*' -m pytest -v -s```, to omit environment from coverage results
9. run: ```coverage report -m```, to get coverage results
10. run: ```coverage html```, to generate htmlcov folder. Then open htmlcov/index.html with live server

### Requirements Gathering for TDD
The purpose of testing this flask application is to test the functionality of the application. The scope of the tests will be to test the database connection to the application, test the data in the parts inventory collection, test if files exist, and test the http routes. The input data that will be required for the tests will include data that will go into our mongodb. The output data will be the bson data. The results of our tests will have a final report. An assumption for testing is that mock data will need to be created since this project requires TDD. Some constraints are time availability and resource limitations. Some risks include test failures and the possibility of having dublicate entries in the db.

### User Story
As a developer, I want to run unit tests for the data in my flask application, so that issues can be identified and fixed before the application is deployed to production. 

As a developer, I want to be able to test that data can be created and retrieved from the database and that the data is correct. 

### Test Cases
1. Create a database with mock data of machinery parts
2. Test the database connection to the application  
3. Test to check the number of entries in the database 
4. Test the db data 
5. Test file path for files 
6. Test content in files
7. Test that the http routes work
8. Test response status codes 

### Test Summary
    • Tested feature: NoSQL Database
    • Test environment: Development
    • Test duration: 2 hours
    • Test coverage: 88%
    • Test results: Pass

### Test Cases Executed
```
Test case: Verify connection to the database
    o Test result: Pass
    o Notes: Tested the database connection by returning the sample data.

Test case: Verify data exists in database
    o Test result: Pass
    o Notes: Tested by returning data from db.

Test case: Verify file paths exist
    o Test result: Pass
    o Notes: Tested the file path to app.py and config.py

Test case: Verify the contents of files
    o Test result: Pass
    o Notes: Tested the contents of the app.py and config.py files 

Test case: Verify http routes work
    o Test result: Pass
    o Notes: Tested the home route, get part by id routes, get all parts routes, post part routes, and delete parts by verifying status codes and json response data.      
    
Test Issues
    • No Issues
    Conclusion: Based on the results of the test cases executed, it can be concluded that the database is functioning as expected. 
```    

#### Get parts
<img width="505" alt="Screenshot 2023-01-29 at 6 07 59 PM" src="https://user-images.githubusercontent.com/104322947/215627757-52b4ce79-14e5-45fe-b8ed-91f63c0b200e.png">

#### Get part by ID
<img width="453" alt="Screenshot 2023-01-29 at 6 10 07 PM" src="https://user-images.githubusercontent.com/104322947/215627801-dcb089d7-bf30-4f4d-8eff-c523e1cede27.png">

#### Post parts
<img width="615" alt="Screenshot 2023-01-29 at 6 13 58 PM" src="https://user-images.githubusercontent.com/104322947/215627839-c9c4ded5-5ad2-4335-8b20-a68dfbe20bad.png">

#### Update parts
<img width="625" alt="Screenshot 2023-01-29 at 6 19 08 PM" src="https://user-images.githubusercontent.com/104322947/215627858-7c36b52f-6887-4177-ac57-25cabdb00178.png">

#### Delete parts
<img width="487" alt="Screenshot 2023-01-29 at 6 20 49 PM" src="https://user-images.githubusercontent.com/104322947/215627880-d5704ad3-c704-4cdd-a366-52f9e6d51d56.png">

#### Testing Report
![Screenshot 2023-01-30 at 4 04 50 PM](https://user-images.githubusercontent.com/104322947/215627928-0900fd81-6b5d-4d8f-89f2-255a22090541.png)

#### Coverage Report
![Screenshot 2023-01-30 at 4 04 10 PM](https://user-images.githubusercontent.com/104322947/215627909-aff7c9d2-d4d9-4b88-bf5a-428042505558.png)




