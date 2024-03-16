import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")
    
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message" : "Item successfully deleted"}
        except KeyError:
            abort(404, message="Item not found")
            
    def put(self, item_id):
        item_data = request.get_json()
        print("This is ITEM_DATA output:", item_data)
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload")
        
        try:
            """
            |= : dictionary merge operator
            Details: https://blog.teclado.com/python-dictionary-merge-update-operators/ 
            """
            item = items[item_id]
            item |= item_data # in place modification of item. 
            
            return item
        except KeyError:
            abort(404, message="Item not found.")
            
@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}
    
    def post(self):
        item_data = request.get_json()
        """
        Here not only do I need to validate that the data exist, I also the TYPE of data being inserted
        e.g. Price should be a float.
        """
        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort (
                400,
                message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload."
            )
        # Want to prevent duplications
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"{item} already exist.")
        
        item_id = uuid.uuid4().hex
        item = {**item_data, "id" : item_id}
        items[item_id] = item
        return item, 201