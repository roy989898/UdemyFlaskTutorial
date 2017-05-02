from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

        return {'item': None}, 404

    def post(self, name):
        request_data = request.get_json(silent=True)

        for item in items:
            if item['name'] == name:
                return {'message': "iteam with name " + name + " already existes"}, 400

        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        for item in items:
            if item['name'] == name:
                items.remove(item)
                return {"message": "item deleted"}

        return {"message": "no item deleted"}

    def put(self, name):
        request_data = request.get_json(silent=True)
        for item in items:
            if item['name'] == name:
                item['name'] = name
                item['price'] = request_data['price']
                return {"message": "item updated"}

        # can't find item
        new_item = {'name': name,
                    'price': request_data['price']
                    }
        items.append(new_item)

        return {"message": "item create"}


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')

app.run(port=4000, debug=True)
