from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from db import db
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True