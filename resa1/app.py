from flask import Flask, request
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

itemsDB = [
    {
        'name' : 'MyItem',
        'price' : 17.99
    },
    {
        'name' : 'Yoda',
        'price' : 250.12
    }
]

class Item(Resource):
    def get(self, name):
        return {'item':   next(filter(lambda x: x["name"] == name, itemsDB), None)}

    def post(self,name):
        pass 
    def delete(self, name):
        pass 
    def put(self, name ):
        pass 

class ItemList(Resource):
    def get(self):
        return {'items' : itemsDB}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port = 8080, debug = True)