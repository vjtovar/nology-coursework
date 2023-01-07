# Flask-API

## Project: Intro to flask-api

### Overview
A Flask app using PostgreSQL with and API generated using Elephant SQL to connect to a database and write queries to pull in the data.

### Specifications
1. Install python
2. Set up virtual environment
3. Install pyenv
4. Install flask
5. Use flask to create http requests for different pages of application.

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
9. Install flask, run: ```pip3 install flask```
10. Create app.py and add imports
11. run: ```export FLASK_APP=app.py```
12. run: ```flask --debug run```, to start the server
13. Create requirements.txt file and add flask, python-dotenv, psycopg2 to top of file
14. run: ```pip3 install -r requirements.txt```, to install flask, python-dotenv, psycopg2
15. run: ```flask --debug run``` or add FLASK_APP=app, FLASK_DEBUG=1 to .env file to automatically have debugger on. This starts the server

## Notes for Postman and ElephantSQL
Postman to add data, elephantsql to see data table

@app.post("/api/room")
SELECT * FROM "public"."rooms" in elephantsql
In postman
change to post http://127.0.0.1:5000/api/room
select body, raw, JSON and enter below to create rooms
{
     "name": "kitchen"
}
Will return below
{
    "id": 1,
    "message": "Room kitchen created"
}

@app.post("/api/temperature")
SELECT * FROM "public"."temperatures" in elephantsql
In postman
change to post http://127.0.0.1:5000/api/temperature
select body, raw, JSON and enter below to add temp to rooms by inputing the id number of the room and temperature you want
{
    "room": 4,
    "temperature": 77
}
Will return below
{
    "message": "Temperature added."
}

@app.get("/api/room/<int:room_id>")
SELECT * FROM "public"."rooms" in elephantsql
In postman
change to get http://127.0.0.1:5000/api/room/1
Will show result below by inputing room id above
{
    "message": "Room retrieved by id",
    "name": "kitchen"
}

@app.post("/api/temperature")
"SELECT COUNT(*) FROM rooms;"
In postman
change to post http://127.0.0.1:5000/api/add_random_data
select body, raw, JSON and enter below to add random temp and dates to rooms by adding amount of datapoint
{
    "amount": 5
}

@app.get("/api/average")
SELECT AVG(temperature) as average FROM temperatures
In postman
change to get http://127.0.0.1:5000/api/average
Will show avg temp for all rooms below 
{
    "average": 73.27
}