from flask import Flask, request
from dotenv import load_dotenv
import os
import psycopg2 # Flask library that allows us to connect to PostgreSQL databases
from datetime import datetime, timezone, timedelta 
import random


load_dotenv() #loads variables from .env file to environment

app = Flask(__name__)

url = os.getenv("DATABASE_URL") # gets variables from environment
connection = psycopg2.connect(url)




CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);" #serial means we don't have to pass value to it, automatically generates id
)

CREATE_TEMPS_TABLE = (
    "CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"
) #This uses a FOREIGN KEY to link the table to the rooms table. All this does is ensure referential integrity (i.e. can't enter a room_id for a room that doesn't exist). Also using ON DELETE CASCADE means that if we delete a room, all its referenced temperatures will be deleted too.

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;" #insert room names, (name)=column we will pass values to, return id to insert temp
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);" #To insert temperatures, %s=values passed in later
)

GLOBAL_NUMBER_OF_DAYS = (
    "SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;" #the number of days that temp average is based on. To calculate how many different days we have stored data. use DATE(date) to turn the date column into a PostgreSQL DATE. use DISTINCT with that, it selects only the different individual dates. If we didn't do this, since we store hours, minutes, and seconds in our table, every row would be different even if the date is the same (since the times would differ)
)

GLOBAL_AVG = "SELECT AVG(temperature) as average FROM temperatures;" #calculate and return the average of all temperature readings in the temperatures table

SELECT_ROOM_BY_ID = (
    "SELECT name FROM rooms WHERE id = (%s);"
)

GET_NUMER_OF_ROOMS = (
    "SELECT COUNT(*) FROM rooms;"
)




@app.get('/')
def home():
    return "Hello Monty!"

@app.post("/api/room") # decorator, tells flask what endpoint to accept data in
def create_room():
    data = request.get_json() #expect json data, client sends a string with specific structure turns it into python dictonary
    name = data["name"] #name is the data, assume client sent us json that has field name inside it
    with connection: #connect to DB
        with connection.cursor() as cursor: #use cursor to interact with DB, fetches records returned by backend. cursor object allows us to insert data into DB or iterate over rows that the DB returns
            cursor.execute(CREATE_ROOMS_TABLE) #cursor with parameter allows user to move in the dataset using scroll, create table and insert the record
            cursor.execute(INSERT_ROOM_RETURN_ID, (name,)) #insert row id, this query takes a value passed in as a tuple (name,)=a tuple with a single value
            room_id = cursor.fetchone()[0] #fetchone to read the data, returns the first row that the cursor gives us. [0]=first column which is id in rooms table
    return {"id": room_id, "message": f"Room {name} created"}, 201  # We return a Python dictionary, which Flask converts to JSON. The return status code is 201, which means "Created". It's a way for our API to tell the client succinctly the status of the request.

@app.post("/api/temperature")
def add_temp():
    data = request.get_json() #expect the client to send a request that contains the temperature reading and the room id
    temperature = data["temperature"] #temperature key of the json payload
    room_id = data["room"] #room key of the json payload

    try: #To make sure connection is closed   
        date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M:%S") # date and time will show up in elephantSQL, if payload doesn't have a date key in it do KeyError
    except KeyError: #will get raised if no date key
        date = datetime.now(timezone.utc) #will get todays date and timezone

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TEMPS_TABLE) #Create the temperature readings table, with its 3 columns (room id, temperature reading, and optional date)
            cursor.execute(INSERT_TEMP, (room_id, temperature, date)) #Insert the temperature reading into the table, pass in 3 values as tuple
    return {"message": "Temperature added."}, 201                


@app.get("/api/room/<int:room_id>") #dynamic url
def get_room(room_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ROOM_BY_ID, (room_id,))
            name = cursor.fetchone()[0]
    return {"name": name, "message": "Room retrieved by id"}, 201 


@app.post("/api/add_random_data")
def add_random_data():
    data = request.get_json()
    amount_to_add = data["amount"] #how many datapoints to add

    try:
        date = datetime.strptime(data["data"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_NUMER_OF_ROOMS) #get number of rooms in database
            numberOfRooms = cursor.fetchone()[0]

            cursor.execute(CREATE_TEMPS_TABLE)

            for i in range(0, int(amount_to_add)):
                tempTemp = random.randint(50, 100) #random tempature value
                room_id = random.randint(1, numberOfRooms) #select random room

                dataDifference = timedelta(random.randint(1, 30)) #subtract 1 to 30 days from current date
                tempDate = date - dataDifference

                cursor.execute(INSERT_TEMP, (room_id, tempTemp, tempDate))

    return {"message": amount_to_add + " Temperature Datapoints added."}, 201    


@app.get("/api/average")
def get_avg_temp():
    with connection: #connect to DB
        with connection.cursor() as cursor:
            cursor.execute(GLOBAL_AVG) #selects avg temp of all temps
            average = cursor.fetchone()[0] #return the data, cursor.fetchone()=selects first row and [0]=selects first column of that row
    return {"average": round(average, 2)}, 200 #status code ok    