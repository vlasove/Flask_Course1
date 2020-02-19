from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from item import Item, ItemList
from user import UserRegister

from security import authenticate, identity
import create_table

app = Flask(__name__)
app.secret_key = "vlasov"
api = Api(app)

jwt = JWT(app,authenticate, identity)


api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)



