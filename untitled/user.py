import sqlite3
from flask_restful import Resource, Api, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # , ensure th is a tupe
        row = result.fetchone()  # only get the first one
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,))  # , ensure th is a tupe
        row = result.fetchone()  # only get the first one
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="must have")
    parser.add_argument('password', type=str, required=True, help="must have")

    def post(self):
        data = UserRegister.parser.parse_args();
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES(NULL,?,?)"

        user = User.find_by_username(data['username'])
        if user is not None:
            return {"message": "User already exist"}, 201
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
