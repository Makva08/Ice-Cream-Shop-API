from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authentification, identity

from resources import ItemList, Item

app = Flask(__name__)
app.secret_key = "TheBestKeptSecret"

jwt=JWT(app, authentification, identity)
api = Api(app)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
app.run(port = 5000, debug = True)