import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE user=?"
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
