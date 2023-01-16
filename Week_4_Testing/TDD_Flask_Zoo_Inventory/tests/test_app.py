import sys
import pytest
import requests
import os
import psycopg2
import app
from app import app, create_app 
import json



test_database = os.getenv("DATABASE_URL")


@pytest.fixture
def setup_database():
    connection = psycopg2.connect(test_database)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS enclosures (id SERIAL PRIMARY KEY, enclosure_names TEXT);")
    sample_data_1 = [
        (4, 'primate'),
        (5, 'aviary'),
    ]
    cursor.executemany("INSERT INTO enclosures VALUES (%s, %s);", sample_data_1)

    cursor.execute("CREATE TABLE IF NOT EXISTS animals (id SERIAL PRIMARY KEY, animal_name TEXT, quantity REAL, enclosure_id INTEGER, FOREIGN KEY(enclosure_id) REFERENCES enclosures(id) ON DELETE CASCADE);")
    sample_data_2 = [
        (4, 'Spider Monkey', 20, 4),
        (5, 'Toucan', 10, 5),
    ]
    cursor.executemany('INSERT INTO animals VALUES(%s, %s, %s, %s)', sample_data_2)
    yield connection, cursor


def test_connection(setup_database):
    connection, cursor = setup_database
    cursor.execute('SELECT * FROM enclosures')
    result = cursor.fetchmany(2)
    assert len(list(result)) == 2

def test_type_enclosures(setup_database):
    connection, cursor = setup_database
    cursor.execute('SELECT enclosure_names FROM enclosures')
    result = cursor.fetchone()
    assert type(result) == tuple
    assert len(list(result)) == 1

def test_type_animals(setup_database):
    connection, cursor = setup_database
    cursor.execute('SELECT * FROM animals')
    result = cursor.fetchone()
    assert type(result) == tuple
    assert len(list(result)) == 4  

def test_enclosure_data(setup_database):
    connection, cursor = setup_database
    cursor.execute('SELECT enclosure_names FROM enclosures WHERE id = 1')
    result = cursor.fetchone()
    assert result[0] == 'primate'   
    cursor.execute('SELECT enclosure_names FROM enclosures WHERE id = 2')
    result = cursor.fetchone()
    assert result[0] == 'aviary'  

def test_animal_data(setup_database):
    connection, cursor = setup_database
    cursor.execute('SELECT animal_name FROM animals WHERE id = 1')
    result = cursor.fetchone()
    assert result[0] == 'Spider Monkey' 
    cursor.execute('SELECT animal_name FROM animals WHERE id = 2')
    result = cursor.fetchone()
    assert result[0] == 'Toucan'  


def test_file_exists():
    assert os.path.exists('./app.py')
    assert os.path.exists('./report.html')

def test_file_contents():
    with open('./app.py', 'r') as f:
        contents = f.read()
    assert "def create_app(config)" in contents 
    with open('./report.html', 'r') as f:
        contents = f.read()
    assert "elem = document" in contents  



@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.data == b"Welcome to the Zoo!"
    assert response.status_code == 200  

def test_enclosure_id_route(client):
    response = client.get('/api/enclosures/1')
    json_response = response.get_json()
    print("getting enclosure id 1: " + str(response.json))
    assert response.status_code == 200
    assert json_response == {"enclosure_names": ["primate"]}

def test_animal_id_route(client):
    response = client.get('/api/animals/1')
    json_response = response.get_json()
    print("getting animal id 1: " + str(response.json))
    assert response.status_code == 200
    assert json_response == {"animal_name": "Spider Monkey", "message": "Animal retrieved by id"}
    
def test_enclosures_route(client):
    response = client.get('/api/enclosures') 
    json_response = response.get_json()
    print("getting enclosures: " + str(response.json))
    assert json_response == {"all_enclosures": [[1, 'primate'], [2, 'aviary'], [3, 'Elephant Odyssey']]}
    assert type([0]) is list
    assert response.status_code == 200

def test_animals_route(client):
    response = client.get('/api/animals') 
    json_response = response.get_json()
    print("getting animals: " + str(response.json))
    assert json_response == {"all_animals": [[1, 'Spider Monkey', 20, 1], [2, 'Toucan', 10, 2], [3, 'Elephant', 15, 3]]}
    assert type(json_response) is dict 
    assert response.status_code == 200

def test_enclosures_count(client):
    response = client.get('/api/enclosures/count') 
    json_response = response.get_json()
    assert json_response == {"count": 3, 'message': 'There are 3 enclosures'} 
    assert response.status_code == 200 

def test_animals_count(client):
    response = client.get('/api/animals/count') 
    json_response = response.get_json()
    assert json_response == {"count": 3, 'message': 'There are 3 animals'} 
    assert response.status_code == 200      
   
 
# def test_adding_enclosures(client):
#     response = client.post('/api/enclosures', json ={
#             "enclosure_names" : "Elephant Odyssey"
#         }) 
#     json_response = response.get_json()
#     print (json_response)
#     assert response.status_code == 201

# def test_adding_animals(client):
#     response = client.post('/api/animals', json ={
#             "animal_name" : "Elephant",
#             "quantity": 15,
#             "enclosure_id": 3, 
#         }) 
#     json_response = response.get_json()
#     print (json_response)
#     assert response.status_code == 201





    







 