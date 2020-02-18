from flask import Flask, request
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

itemsDB = []

class Item(Resource):
    def get():
        pass 
    def post():
        pass 
    def delete():
        pass 
    def put():
        pass 

class ItemList(Resource):
    def get():
        pass 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port = 8080, debug = True)