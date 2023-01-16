from flask import Flask, request, jsonify, abort, make_response
from dotenv import load_dotenv
import os
import psycopg2 
import logging
import csv
from datetime import date



load_dotenv() 

app = Flask(__name__)
url = os.getenv("DATABASE_URL") 
connection = psycopg2.connect(url)



today = date.today()
logging.basicConfig(
    filename='test.log', 
    filemode='w',
    level=logging.DEBUG, 
    format="{asctime} {levelname:<8} {message}", 
    style ='{', 
)

logging.debug('This is a Debug msg')
logging.info('This is a Info msg')
logging.warning('This is a Warning msg')
logging.error('This is an Error msg')

with open('test.log', 'r') as logfile, open('test.csv', 'w') as csvfile:
    reader = csv.reader(logfile, delimiter='|')
    writer = csv.writer(csvfile, delimiter='|',)
    writer.writerow(['column1', 'column2', 'column3', 'column4'])
    writer.writerows(reader)       



CREATE_ENCLOSURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, enclosure_names TEXT);"
)

CREATE_ANIMALS_TABLE = (
    "CREATE TABLE IF NOT EXISTS animals (id SERIAL PRIMARY KEY, animal_name TEXT, quantity REAL, enclosure_id INTEGER, FOREIGN KEY(enclosure_id) REFERENCES enclosures(id) ON DELETE CASCADE);"
)

INSERT_ENCLOSURE_RETURN_ID = ("INSERT INTO enclosures (enclosure_names) VALUES (%s) RETURNING id;")

INSERT_ANIMAL_RETURN_ID = ("INSERT INTO animals (animal_name, quantity, enclosure_id) VALUES (%s, %s, %s) RETURNING id;"
)
    
SELECT_ALL_ENCLOSURES = (
    "SELECT * FROM enclosures;"
)

SELECT_ENCLOSURE_BY_ID = (
     "SELECT enclosure_names FROM enclosures WHERE id = (%s);"
)

SELECT_ALL_ANIMALS = (
    "SELECT * FROM animals;"
)
SELECT_ANIMAL_BY_ID = (
    "SELECT animal_name FROM animals WHERE id = (%s);"
)

GET_NUMBER_OF_ENCLOSURES =(
    "SELECT COUNT(*) FROM enclosures;"
)

GET_NUMBER_OF_ANIMALS =(
    "SELECT COUNT(*) FROM animals;"
)



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def home():
        return 'Welcome to the Zoo!'


    @app.post("/api/enclosures")
    def create_enclosure():
        data = request.get_json()
        enclosure_names = data["enclosure_names"]
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_ENCLOSURES_TABLE)
                cursor.execute(INSERT_ENCLOSURE_RETURN_ID, (enclosure_names,))
                enclosure_id = cursor.fetchone()[0]
            return {"id": enclosure_id, "message": f"Enclosure {enclosure_names} created"}, 201  
                
            
    @app.post("/api/animals")
    def create_animal():
        data = request.get_json()
        animal_name = data["animal_name"]
        quantity = data["quantity"]
        enclosure_id = data['enclosure_id']
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_ANIMALS_TABLE)
                cursor.execute(INSERT_ANIMAL_RETURN_ID, (animal_name, quantity, enclosure_id))
                animal_id = cursor.fetchone()[0]
                return {"id": animal_id, "message": f"Animals {animal_name} created"}, 201


    @app.get("/api/enclosures/<int:enclosure_id>")
    def get_enclosure(enclosure_id):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ENCLOSURE_BY_ID, (enclosure_id, ))
                enclosure_names= cursor.fetchone()
                return {"enclosure_names": enclosure_names}, 200 


    @app.get("/api/animals/<int:animal_id>")
    def get_animal(animal_id):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ANIMAL_BY_ID, (animal_id,))
                animal_name = cursor.fetchone()[0]
                return {"animal_name": animal_name, "message": "Animal retrieved by id"}, 200 
    
            
    @app.get("/api/enclosures")
    def get_enclosures():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_ENCLOSURES)
                all_enclosures = cursor.fetchall()
                return {"all_enclosures": all_enclosures}, 200


    @app.get("/api/animals")
    def get_animals():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_ANIMALS)
                all_animals = cursor.fetchall()
                return {"all_animals": all_animals}, 200


    @app.get("/api/enclosures/count")
    def get_count_enclosures():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_NUMBER_OF_ENCLOSURES)
                count = cursor.fetchone()[0]
                return {"count": count, "message": f"There are {count} enclosures"}, 200


    @app.get("/api/animals/count")
    def get_count_animals():
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(GET_NUMBER_OF_ANIMALS)
                count = cursor.fetchone()[0]
                return {"count": count, "message": f"There are {count} animals"}, 200                                  


    #error handling
    # @app.errorhandler(404)
    # def not_found(error):
    #     return make_response(jsonify({"error": "not found!"}), 404)

    # @app.errorhandler(400)
    # def not_found(error):
    #     return make_response(jsonify({"error": "Bad request!"}), 400)         
    

    return app
    
app = create_app({"TESTING": True})  

if __name__ == "__main__":
    app.run


























