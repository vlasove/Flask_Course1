from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3 


class Item(Resource):
    TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument("price",
            type=float,
            required=True,
            help = "This field cannot be blank!"
    )

    @classmethod
    def find_by_name(cls, name):
        pass 

    @classmethod
    def insert(cls, item):
        pass 

    @classmethod
    def update(cls, item):
        pass 

    @jwt_required()
    def get(self,name):
        pass

    @jwt_required()
    def post(self,name):
        pass

    @jwt_required()
    def put(self, name):
        pass

    @jwt_required()
    def delete(self, name):
        pass 

class ItemList(Resource):
    TABLE_NAME = 'items'
    def get(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cur.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0], 'price':row[1]})
        conn.close()
        return {'items' : items}
