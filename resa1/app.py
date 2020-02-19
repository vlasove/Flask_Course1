from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

from security import authenticate, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = "vlasov"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    from db import db
    db.init_app(app) 
    app.run(host='0.0.0.0', debug = True)



