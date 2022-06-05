from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        stores=StoreModel.find_by_name(name)
        if stores:
            return stores.json()
        else:
            return {"message":" Store not found"}
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message":"store already present"}
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"Something went wrong"}
        return store.json(),200

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        else:
            return {"message":"Store not present to delete"}

class StoreList(Resource):
    def get(self):
        return {"stores":[ store.json() for store in StoreModel.query.all() ]}