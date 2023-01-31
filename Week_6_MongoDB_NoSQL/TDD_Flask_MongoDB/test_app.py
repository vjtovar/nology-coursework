import pytest
import os
from app import app
from app import get_app_with_config
from config import TestConfig
import json
from bson.objectid import ObjectId



app, mongo = get_app_with_config(TestConfig)


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client(app) as client:
        yield client


def test_index(client):
    response = client.get('/')
    my_json = response.data.decode("UTF-8")
    print(my_json)
    data = json.loads(my_json)
    print(data)
    assert response.status_code == 200
    

def test_get_item(client):
    response = client.get('/item/63d34e61cc7415434112104b')
    my_json = response.data.decode("UTF-8")
    print(my_json)
    data = json.loads(my_json)
    assert data == {'_id': {'$oid': '63d34e61cc7415434112104b'}, 'part_number': 57896, 'part_name': 'washer', 'quantity': 5, 'quantity_order': 545, 'reorder_level': 10, 'backordered': True, 'cost': 45, 'dimensions(mm)': '2X2'}
    assert response.status_code == 200


def test_db_item(client):
    sample_object_id = ObjectId('63d336c5c60def51de595ba4')
    result = client.get(f'/item/{sample_object_id}')
    assert result.status_code == 404 
    print(result) 


def test_create_item(client):
    response = client.post('/item', json= {
        'part_number': 57896, 
        'part_name': 'washer', 
        'quantity': 5, 
        'quantity_order': 65, 
        'reorder_level': 10, 
        'backordered': True, 
        'cost': 45, 
        'dimensions(mm)': "1X2"
        })
    assert response.status_code == 200


def test_delete_item(client):
    sample_object_id = ObjectId('63d73a09b2487205652ca7a0')
    result = client.delete(f'/item/{sample_object_id}')
    assert result.status_code == 200
    print(result)


def test_item_deleted(client):
    sample_object_id = ObjectId('63d73693d5a741a0e8b3a33a')
    result = client.delete(f'/item/{sample_object_id}')
    assert result.status_code == 404
    print(result)    


def test_file_exists():
    assert os.path.exists('./app.py')
    assert os.path.exists('./config.py')

def test_file_contents():
    with open('./app.py', 'r') as f:
        contents = f.read()
    assert "app = Flask(__name__)" in contents 
    with open('./config.py', 'r') as f:
        contents = f.read()
    assert "MONGO_HOST" in contents  


# def test_update_item(client):
#     new_data = {
#         'part_number': 57896, 
#         'part_name': 'washer', 
#         'quantity': 5, 
#         'quantity_order': 545, 
#         'reorder_level': 10, 
#         'backordered': False, 
#         'cost': 45, 
#         'dimensions(mm)': "2X2"
#         }
#     response = client.get('/item/63d72a2c197848d98d867b45')
#     {"_id": ObjectId('63d72a2c197848d98d867b45')}, {"$set": new_data},
#     assert response.status_code == 200
#     print(response)        