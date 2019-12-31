from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Section_6.resources.item import Item, ItemList
from Section_6.resources.store import Store, StoreList
from Section_6.resources.user import UserRegister
from Section_6.security import authenticate, identity
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.secret_key = 'alex'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
