import uuid
from flask import Flask, request
from db import stores, items
from flask_smorest import abort  

app = Flask(__name__)

# ----------------- GET STORE
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

# ----------------- POST STORE

@app.post("/store")
def create_store():
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

# ----------------- DEL STORE

@app.delete("/item/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message" : "Deleted store"}
    except KeyError:
        abort(404, message="Store not found")
 

# ----------------- GET ALL ITEMS

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

# ----------------- GET ITEM

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")

@app.get("/item/<string:item_id>")
def get_item_in_store(item_id):
   try:
       return items[item_id]
   except KeyError:
       abort(404, message="Item not found")

# ----------------- POST ITEM

@app.post("/item")
def create_item():
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
    
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id" : item_id}
    items[item_id] = item
    return item, 201

# ----------------- DELETE ITEM
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message" : "Item successfully deleted"}
    except KeyError:
        abort(404, message="Item not found")

# ----------------- UPDATE ITEM   
@app.put("/item/<string:item_id>")
def update_item(item_id):
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