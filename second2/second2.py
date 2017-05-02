from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


app.run(port=4000)
