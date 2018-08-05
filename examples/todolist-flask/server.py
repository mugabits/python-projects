# server.py

import json
from flask import Flask, make_response

app = Flask(__name__)

FAKE_DATA = {
    "item"
}


@app.route("/")
def home():
    return make_response("This is home", 200)


@app.route("/items", methods=["GET"])
def all_items():
    return make_response("[]", 200)


@app.route("/items", methods=["POST"])
def create_items():
    data = {
        "item": "Go to ATM",
        "item_id": 1,
        "item_description": "Get money"
        }
    return make_response(json.dumps(data), 201)


@app.route("/items/<int:item_id>/", methods=["GET"])
def item_id(item_id):
    item_info = {
        "item": "Go to ATM",
        "item_id": 1,
        "item_description": "Get money"
    }
    return make_response(json.dumps(item_info), 200)

if __name__ == "__main__":
    app.run()
