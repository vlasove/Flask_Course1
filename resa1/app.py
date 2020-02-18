from flask import Flask, request
from flask_restful import Resource, Api, reqparse 

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
        return {'item':   next(filter(lambda x: x["name"] == name, itemsDB), None)}, 200

    def post(self,name):
        if next(filter(lambda x: x["name"] == name, itemsDB), None)  is not None:
            return {"message": "This item already exists"}
        parser = reqparse.RequestParser()
        parser.add_argument("price",
            type=float,
            required=True,
            help = "This field cannot be blank!"
        )

        data = parser.parse_args()
        new_item = {"name" : name , "price" : data["price"]}
        itemsDB.append(new_item)
        return new_item

    def delete(self, name):
        global itemsDB
        itemsDB = list(filter(lambda  x : x["name"] != name, itemsDB)) 
        return {"message":"Item deleted"}, 202


    def put(self, name ):
        parser = reqparse.RequestParser()
        parser.add_argument("price",
            type=float,
            required=True,
            help = "This field cannot be blank!"
        )

        data = parser.parse_args()

        item =  next(filter(lambda x: x["name"] == name, itemsDB), None)
        if item is None:
            new_item = {"name": name, "price" : data["price"]}
            itemsDB.append(new_item)
        else:
            item.update(data) #item - referal changing price
        return item 

class ItemList(Resource):
    def get(self):
        return {'items' : itemsDB}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port = 8080, debug = True)



