from app.database import get_database
from bson.objectid import ObjectId
from app.models.v1.api.advertisements import UpdateAdvertisement, AdvertisementAPI, CreateAdvertisement
from app.models.v1.db.advertisements import AdvertisementDB
from typing import List
from fastapi.responses import JSONResponse

class AdvertisementCRUD:
    def __init__(self, db):
        self.db = db
        self.collection = db["advertisements"]
        
    def get_list(self) -> List[AdvertisementDB]:
        advs = self.collection.find()
        response = [AdvertisementDB(**adv) for adv in advs]
        return response 

    def get(self, adv_id: str) -> AdvertisementDB:
        adv = self.collection.find_one({"_id": ObjectId(adv_id)})
        if not adv:
            return JSONResponse(status_code=404, content='Not found')
        return AdvertisementDB(**adv)
        
    def create(self, adv_request: CreateAdvertisement) -> AdvertisementDB:
        result = self.collection.insert_one(dict(adv_request))
        adv = self.collection.find_one({"_id": result.inserted_id})
        if not adv:
            return JSONResponse(status_code=400, content='Not created')  
        return AdvertisementDB(**adv)

    def update(self, adv_id: str, adv_request: UpdateAdvertisement) -> AdvertisementDB:
        result = self.collection.find_one_and_update({"_id": ObjectId(adv_id)}, {"$set": dict(adv_request)})
        adv = self.collection.find_one({"_id": result["_id"]})
        if not adv:
            return JSONResponse(status_code=404, content='Not found')
        return AdvertisementDB(**adv)

    def delete(self, adv_id: str) -> JSONResponse:
        result = self.collection.delete_one({"_id":ObjectId(adv_id)})
        if result.deleted_count == 0:
            return JSONResponse(status_code=404, content='Not found')
        return JSONResponse(status_code=200, content="Deleted successfully")