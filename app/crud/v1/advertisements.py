from app.database import get_database
from bson.objectid import ObjectId
from app.models.v1.api.advertisements import UpdateAdvertisement, AdvertisementAPI, CreateAdvertisement
from app.models.v1.db.advertisements import AdvertisementDB
from typing import List
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app.exceptions.v1.error_handlers import CustomException

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
            raise CustomException(status_code=404, detail="Not found")
        return AdvertisementDB(**adv)
        
    def create(self, adv_request: CreateAdvertisement) -> JSONResponse | ObjectId:
        result = self.collection.insert_one(dict(adv_request))
        if not result.inserted_id:
            raise CustomException(status_code=400, detail="Not created")  
        return result.inserted_id

    def update(self, adv_id: str, adv_request: UpdateAdvertisement) -> ObjectId | JSONResponse:
        result = self.collection.find_one_and_update({"_id": ObjectId(adv_id)}, {"$set": adv_request.model_dump(exclude_none=True)})
        if not result["_id"]:
            raise CustomException(status_code=404, detail="Not found")
        return result["_id"]

    def delete(self, adv_id: str) -> JSONResponse:
        result = self.collection.delete_one({"_id":ObjectId(adv_id)})
        if not result.deleted_count:
            raise CustomException(status_code=404, detail="Not found")