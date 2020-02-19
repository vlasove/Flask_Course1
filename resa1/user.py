import sqlite3 
from flask_restful import Resource, reqparse

class User:
    TABLE_NAME = 'users'

    def __init__(self, id, username, password):
        self.id = id 
        self.username = username 
        self.password = password 
    
    @classmethod 
    def find_by_username(cls, username):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        query = "SELECT * FROM {table} WHERE username = ?".format(table=cls.TABLE_NAME)
        result = cur.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2]) 
        else:
            user = None

        conn.close() 
        return user


    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        query = "SELECT * FROM {table} WHERE id = ?".format(table=cls.TABLE_NAME)
        result = cur.execute(query, (id,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2]) 
        else:
            user = None

        conn.close() 
        return user


class UserRegister(Resource):
    TABLE_NAME = "users"

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table = self.TABLE_NAME)
        cur.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return {'message' : "User created"}, 201
