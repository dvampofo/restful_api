import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
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
    
    @blp.arguments(ItemUpdateSchema)  
    @blp.response(200, ItemSchema)  
    def put(self, item_data, item_id):
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
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values() #returns a list of vals
    
    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
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