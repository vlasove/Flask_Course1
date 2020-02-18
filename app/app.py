from flask import Flask , jsonify, request

app = Flask(__name__)
# POST --- получить данные
# GET --- послать клиенту ответ (данные)

storesDB = [
    {
        'name':'SpecialistStore',
        'items':[
            {
                'name' : 'Banana',
                'price': 70.23
            },
            {
               'name' : 'Apple',
               'price': 52.23 
            }
        ]
    }
]

#GET /stores 
@app.route('/stores', methods=["GET"])
def get_stores():
    return jsonify({'stores': storesDB}), 200


#POST /store + data : {name:}
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name' : data['name'],
        'items' : []
    }
    storesDB.append(new_store)
    return jsonify(new_store), 201





#GET /store/<string:name>
@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    for store in storesDB:
        if store["name"] == name:
            return jsonify(store),200
    return jsonify({"message" : "store not found"}), 204

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    for store in storesDB:
        if store["name"] == name:
            new_item = {
                "name" : data["name"],
                "price" : data["price"]
            }
            store["item"].append(new_item)
            return jsonify(new_item), 201
    return jsonify({"message" : "store not found"}), 204


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=["GET"])
def get_item_in_store(name):
    for store in storesDB:
        if store["name"] == name:
            return jsonify({"items":store["items"]}),200
    return jsonify({"message":"store not found"}), 204



app.run(port=8080, debug=True)


