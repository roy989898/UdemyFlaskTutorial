from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# post  use to receive data,for server
# get used to send data to client only

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass


# GET /store
@app.route('/store/', methods=['GET'])
def get_store():
    pass


# POST /store/<string:name>/item {name:,price:}
@app.route('store/<string:name>/item')
def create_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_store(name):
    pass


if __name__ == '__main__':
    app.run(port=5000)
