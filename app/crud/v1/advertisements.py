from app.database import get_database
from bson.objectid import ObjectId
from app.models.v1.api.advertisements import UpdateAdvertisement, AdvertisementAPI, CreateAdvertisement
from app.models.v1.db.advertisements import AdvertisementDB
from typing import List
from fastapi.responses import JSONResponse

class Advertisement:
    def __init__(self, db):
        self.db = db
        self.collection = db["advertisements"]
        
    def get_list(self) -> List[AdvertisementDB]:
        advs = self.collection.find()
        response = [AdvertisementDB(**adv) for adv in advs]
        return response 

    def get(self, adv_id: str) -> JSONResponse | AdvertisementDB:
        adv = self.collection.find_one({"_id": ObjectId(adv_id)})
        if not adv:
            return JSONResponse(status_code=404, content='Not found')
        return AdvertisementDB(**adv)
        
    def create(self, adv_request: CreateAdvertisement) -> JSONResponse | str:
        result = self.collection.insert_one(dict(adv_request))
        if not result.inserted_id:
            return JSONResponse(status_code=400, content='Not created')  
        return str(result.inserted_id)

    def update(self, adv_id: str, adv_request: UpdateAdvertisement) -> JSONResponse:
        result = self.collection.find_one_and_update({"_id": ObjectId(adv_id)}, {"$set": adv_request.model_dump(exclude_none=True)})
        if not result["_id"]:
            return JSONResponse(status_code=404, content='Not found')
        return JSONResponse(status_code=200, content="Updated successfully")

    def delete(self, adv_id: str) -> JSONResponse:
        result = self.collection.delete_one({"_id":ObjectId(adv_id)})
        if not result.deleted_count:
            return JSONResponse(status_code=404, content='Not found')
        return JSONResponse(status_code=200, content="Deleted successfully")