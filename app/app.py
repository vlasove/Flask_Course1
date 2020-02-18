from flask import Flask , jsonify

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
    return jsonify({'stores': storesDB})
#POST /store + data : {name:}
#GET /store/<string:name>
@app.route('/store/<string:name>', methods=["GET"])
def get_store(name):
    for store in storesDB:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message" : "store not found"})

#POST /store/<string:name>/item {name:, price:}
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=["GET"])
def get_item_in_store(name):
    for store in storesDB:
        if store["name"] == name:
            return jsonify({"items":store["items"]})
    return jsonify({"message":"store not found"})



app.run(port=8080, debug=True)