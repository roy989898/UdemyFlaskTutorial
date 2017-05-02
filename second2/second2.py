from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app, authenticate, identity)  # /auth

items = []


def find_item_in_list(item_list, item_name):
    for item in item_list:
        if item['name'] == item_name:
            return item
    return None


class Item(Resource):
    @jwt_required()
    def get(self, name):
        finded_item = find_item_in_list(items, name)

        if finded_item is not None:
            return finded_item
        else:
            return {'item': None}, 404

    def post(self, name):
        request_data = request.get_json(silent=True)
        finded_item = find_item_in_list(items, name)

        if finded_item is not None:
            return {'message': "iteam with name " + name + " already existes"}, 400
        else:
            item = {'name': name, 'price': request_data['price']}
            items.append(item)
            return item, 201

    def delete(self, name):

        finded_item = find_item_in_list(items, name)

        if finded_item is not None:
            items.remove(finded_item)
            return {"message": "item deleted"}
        else:
            return {"message": "no item deleted"}

    def put(self, name):
        request_data = request.get_json(silent=True)

        finded_item = find_item_in_list(items, name)

        if finded_item is not None:
            finded_item['name'] = name
            finded_item['price'] = request_data['price']
            return {"message": "item updated"}
        else:
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
