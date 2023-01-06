
## Commands for setting up env and flask api
$ mkdir flask-api
$ cd flask-api
$ python3 -m venv env
$ source env/bin/activate 
$ code .
$ pyenv local 3.10.7
$ pyenv local
$ pip3 install flask
<!-- create app.py and add imports -->
$ export FLASK_APP=app.py
$ flask --debug run
<!-- create file and add flask, python-dotenv, psycopg2 to top of file-->
$ pip install -r requirements.txt
$flask --debug run

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