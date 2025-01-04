from app.v1.database import get_database
from bson.objectid import ObjectId

class Advertisement:
    def __init__(self, db):
        self.db = db
        self.collection = db["advertisement"]
        
    def get_advertisements(self):
        advs = []
        for adv in self.collection.find():
            adv['_id'] = str(adv['_id'])
            advs.append(adv)
        return advs

    def get_advertisement(self, adv_id):
        response = self.collection.find_one({"_id": ObjectId(adv_id)})
        if response:
            response["_id"] = str(response["_id"])
            return response
        return {"message": "404 Not Found"}

    def create_advertisement(self, adv_request):
        self.collection.insert_one(dict(adv_request))
        return {"message": "Created successfully"}

    def update_advertisement(self, adv_id, adv_request):
        self.collection.update_one({"_id": ObjectId(adv_id)}, {"$set": dict(adv_request)})
        return {"message": "Updated successfully"}

    def delete_advertisement(self, adv_id):
        self.collection.delete_one({"_id":ObjectId(adv_id)})
        return {"message": "Deleted successfully"}