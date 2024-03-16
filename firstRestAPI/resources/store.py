import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

# Blueprint is used to divide the API into multiple segments
blp = Blueprint("stores", __name__, description="Operations on stores")

# Methodview: creates class whose methods routes to different endpoints 

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
          return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")
    
    def delete(self, store_id):
        try:
             del stores[store_id]
             return {"message" : "Deleted store"}
        except KeyError:
             abort(404, message="Store not found")
             

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    
    def post(self):
        # json string turned into python dict
        store_data = request.get_json()
        if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload."
            )
        #  checking if store already exist
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"'{store}' already exist.")
        store_id = uuid.uuid4().hex # creates UUID
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201

