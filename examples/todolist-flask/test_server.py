# test_server.py

import doctest
import unittest
import json

from server import app
app.testing = True


def body(response):
    return json.loads(response.data.decode("utf-8"))


class TestServer(unittest.TestCase):
    def test_retrieve_all_items(self):
        test_client = app.test_client()
        r = test_client.get("/items")
        self.assertEqual(200, r.status_code)
        self.assertEqual([], body(r))

    def test_create_items(self):
        test_client = app.test_client()
        test_data = json.dumps({
            "item": "Go to ATM",
            "description": "Cash for Games"
        })

        r = test_client.post("/items", data=test_data)
        self.assertEqual(201, r.status_code)
        data = body(r)
        self.assertIn("item_id", data)
        item_id = data["item_id"]
        r = test_client.get("/items/{:d}/".format(item_id))
        self.assertEqual(200, r.status_code)
        item = body(r)
        self.assertEqual(item_id, item["item_id"])
        self.assertEqual("Go to ATM", item["item_description"])