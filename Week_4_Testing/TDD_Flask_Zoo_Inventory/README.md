# TDD_Flask_Zoo_Inventory

## Project: TDD Unit Testing

### Overview
Unit Testing using TDD before creating a Flask app with and API generated using ElephantSQL to connect to a zoo inventory database and write queries to pull in the data.

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

### Pytest Installation
1. Install pytest, run: ```pip3 install pytest```
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
The purpose of testing this flask application is to test the functionality of the application. The scope of the tests will be to test the database connection to the application, test the data in the animals/enclosure table, test if files exist, and test the http routes. The input data that will be required for the tests will include data that will go into our animal table (id,  animal name, quantity of animals, enclosure id) and enclosure table (id, enclosure name). The output data will be the enclosure table and animal table. The results of our tests will have a final report. An assumption for testing is that mock data will need to be created since this project requires TDD. Some constraints are time availability and resource limitations. Some risks include test failures and the possibility of having dublicate entries in the tables.

### User Story
As a developer, I want to run unit tests for the data in my flask application, so that issues can be identified and fixed before the application is deployed to production. 

As a developer, I want to be able to test that enclosures and animals can be created and retrieved from the database and that the data is correct. 

### Test Cases
1. Create a database with mock data of enclosure table and animal table 
2. Test the database connection to the application  
3. Test to check the number of entries in the database 
4. Test the table data. Test the data types and lengths 
5. Test file path for files 
6. Test content in files
7. Test that the http routes work
8. Test response status codes 

### Test Summary
    • Tested feature: Database Relational Tables
    • Test environment: Development
    • Test duration: 2 hours
    • Test coverage: 91%
    • Test results: Pass

### Test Cases Executed
```
Test case: Verify connection to the database
    o Test result: Pass
    o Notes: Tested the database connection by creating sample data and checking the length of the sample data.

Test case: Verify data types, lengths, and values in tables
    o Test result: Pass
    o Notes: Tested enclosure and animal data types, lengths, and values in tables.

Test case: Verify file paths exist
    o Test result: Pass
    o Notes: Tested the file path to app.py and report.html

Test case: Verify the contents of files
    o Test result: Pass
    o Notes: Tested the contents of the app.py and report.html files 

Test case: Verify http routes work
    o Test result: Pass
    o Notes: Tested the home route, get enclosure/animal by id routes, get all enclosures/animals routes, and post enclosure/animal routes by verifying status codes and json response data.      
    
Test Issues
    • One Issue
    Conclusion: Based on the results of the test cases executed, it can be concluded that the database relational tables are functioning as expected. One issue was encountered: The post routes are working, but tests are inserting data into the database.
```    

#### Post enclosures
![Screenshot 2023-01-16 at 9 21 15 AM](https://user-images.githubusercontent.com/104322947/212749579-81b18b73-6a0b-4419-aac7-92ba5a2a1c72.png)

#### Post animals
![Screenshot 2023-01-16 at 9 36 51 AM](https://user-images.githubusercontent.com/104322947/212749619-c80c90fe-2cee-4fd6-af5c-a8a534391545.png)

#### Get enclosures
![Screenshot 2023-01-16 at 9 37 46 AM](https://user-images.githubusercontent.com/104322947/212749656-236aeca5-a8bd-46c7-8aad-d4ef1598ca40.png)

#### Get animals
![Screenshot 2023-01-16 at 9 38 25 AM](https://user-images.githubusercontent.com/104322947/212749676-0d73a9b0-18e4-45c6-b96d-9f57bfafec95.png)

#### Enclosure Table
![Screenshot 2023-01-16 at 9 57 20 AM](https://user-images.githubusercontent.com/104322947/212749778-a572ffba-eb29-45c2-a84e-256a08a48825.png)

#### Animal Table
![Screenshot 2023-01-16 at 9 56 54 AM](https://user-images.githubusercontent.com/104322947/212749832-f519d755-f6ca-4733-843c-6455b4842edb.png)

#### Testing Report
![Screenshot 2023-01-16 at 11 03 40 AM](https://user-images.githubusercontent.com/104322947/212750003-b74e4b1b-8621-4b4f-b1a0-71d2e4effc20.png)

#### Coverage Report
![Screenshot 2023-01-20 at 10 35 44 AM](https://user-images.githubusercontent.com/104322947/213779592-40ba12fe-eb75-4844-b088-90b0ce8585f8.png)




