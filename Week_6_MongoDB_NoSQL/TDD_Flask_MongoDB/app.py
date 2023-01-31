from flask import Flask, request
from pymongo import MongoClient
from mongopass import mongopass
from bson import json_util
from bson.objectid import ObjectId
import json
from flask_pymongo import PyMongo
from config import TestConfig


def get_app_with_config(config):
    app = Flask(__name__)
    app.config.from_object(config)
    mongo = PyMongo(app)


    client = MongoClient(mongopass)
    db = client["crud"]
    collection = db["parts"]

    @app.route("/")
    def index():
        data = []
        for d in collection.find():
            data.append(d)
        return json.dumps(data, indent=4, default=json_util.default), 200

    @app.route("/item/<item_id>")
    def get_item(item_id):
        item = collection.find_one({"_id": ObjectId(item_id)})
        if item:
            return json_util.dumps(item), 200
        else: 
            return json_util.dumps({"error": "Item not found."}), 404


    @app.route("/item", methods=["POST"])
    def create_item():
        item = request.get_json()
        result = collection.mongo.db.insert_one(item)
        return json_util.dumps({"_id": str(result.inserted_id)})


    @app.route("/item/<item_id>", methods=["PUT"])
    def update_item(item_id):
        item = request.get_json()
        result = collection.mongo.db.update_one({"_id": ObjectId(item_id)}, {"$set": item})
        if result.matched_count > 0:
            return json_util.dumps({"status": "success"})
        else:
            return json_util.dumps({"error": "Item not found."}), 404 

    @app.route("/item/<item_id>", methods=["DELETE"])
    def delete_item(item_id):
        result = collection.mongo.db.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count > 0:
            return json_util.dumps({"status": "success"})
        else:
            return json_util.dumps({"error": "Item not found."}), 404 


     
    return app, mongo

app, mongo = get_app_with_config(TestConfig)

if __name__ == '__main__':
    app.run(DEBUG = True)


                



   