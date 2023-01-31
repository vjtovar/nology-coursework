from flask import Flask, request
from pymongo import MongoClient
from mongopass import mongopass
from bson import json_util
from bson.objectid import ObjectId
import json

app = Flask(__name__)

client = MongoClient(mongopass)
db = client["Cluster0"]
collection = db["addColl"]

@app.route("/")
def index():
    # empty string to add for loop iterations
    data = []
    # for loop to iterate collection items
    for d in collection.find():
        data.append(d)
        # return collection
    return json.dumps(data, indent=4, default=json_util.default), 200


@app.route("/item/<item_id>")
def get_item(item_id):
    # find one item by _id
    item = collection.find_one({"_id": ObjectId(item_id)})
    #logic to determine if item present
    if item:
        return json_util.dumps(item), 200
    else: 
        return json_util.dumps({"error": "Item not found."}), 404


@app.route("/item", methods=["POST"])
def create_item():
    # pulls request of JSON from front end or Postman/Insomnia
    item = request.get_json()
    #inserts item into MongoDB Collection
    result = collection.insert_one(item)
    # returns _id of newly insterted item
    return json_util.dumps({"_id": str(result.inserted_id)})


@app.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    item = request.get_json()
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item})
    if result.matched_count > 0:
        return json_util.dumps({"status": "success"})
    else:
        return json_util.dumps({"error": "Item not found."}), 404 

@app.route("/item/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count > 0:
        return json_util.dumps({"status": "success"})
    else:
        return json_util.dumps({"error": "Item not found."}), 404               



if __name__ == '__main__':
    app.run(DEBUG=True)    