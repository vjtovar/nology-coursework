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

<img width="1221" alt="Screenshot 2023-01-07 at 2 19 54 PM" src="https://user-images.githubusercontent.com/104322947/211172457-32279165-b75b-48e9-9923-7ea042534879.png">

<img width="856" alt="Screenshot 2023-01-07 at 2 20 21 PM" src="https://user-images.githubusercontent.com/104322947/211172485-b0e28e97-924b-497f-8fb3-52e9a35f2bbb.png">



```
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
```

<img width="724" alt="Screenshot 2023-01-07 at 2 10 53 PM" src="https://user-images.githubusercontent.com/104322947/211172510-38fe09ba-1619-4880-9529-90db11185261.png">



```
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
```

<img width="854" alt="Screenshot 2023-01-07 at 2 12 11 PM" src="https://user-images.githubusercontent.com/104322947/211172545-8075056e-e615-4312-9357-a48e9bdc9e2e.png">



```
@app.get("/api/room/<int:room_id>")
SELECT * FROM "public"."rooms" in elephantsql
In postman
change to get http://127.0.0.1:5000/api/room/1
Will show result below by inputing room id above
{
    "message": "Room retrieved by id",
    "name": "kitchen"
}
```

<img width="848" alt="Screenshot 2023-01-07 at 2 14 01 PM" src="https://user-images.githubusercontent.com/104322947/211172574-34454d34-f6e6-4f3f-abae-8cef33fbd8f6.png">



```
@app.post("/api/temperature")
"SELECT COUNT(*) FROM rooms;"
In postman
change to post http://127.0.0.1:5000/api/add_random_data
select body, raw, JSON and enter below to add random temp and dates to rooms by adding amount of datapoint
{
    "amount": 5
}
```

<img width="848" alt="Screenshot 2023-01-07 at 2 17 24 PM" src="https://user-images.githubusercontent.com/104322947/211172590-0f8eb30d-2ea6-4201-9a46-19ee673de2c3.png">



```
@app.get("/api/average")
SELECT AVG(temperature) as average FROM temperatures
In postman
change to get http://127.0.0.1:5000/api/average
Will show avg temp for all rooms below 
{
    "average": 73.27
}
```

<img width="851" alt="Screenshot 2023-01-07 at 2 18 42 PM" src="https://user-images.githubusercontent.com/104322947/211172604-e78675d7-80b8-42c5-919a-b1f63b6116c5.png">

