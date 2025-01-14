from app.crud.v1.advertisements import Advertisement as AdvertisementCrud
from app.models.v1.api.advertisements import AdvertisementAPI
from app.models.v1.api.advertisements import UpdateAdvertisement, CreateAdvertisement
from pymongo.database import Database
from fastapi.responses import JSONResponse
from typing import List
from fastapi import HTTPException
from app.exceptions.v1.error_handlers import CustomException


class Advertisement:
    def __init__(self, db: Database):
        self.db = AdvertisementCrud(db)

    def get_advertisements(self) -> List[AdvertisementAPI]:
        advs = self.db.get_list()
        return [AdvertisementAPI(**adv.model_dump()) for adv in advs]

    def get_advertisement(self, adv_id: str) -> AdvertisementAPI | JSONResponse:
        try:
            adv = self.db.get(adv_id)
            return AdvertisementAPI(**adv.model_dump())
        except:
            raise CustomException(status_code=404, detail="Not found")

    def create_advertisement(self, adv_request: CreateAdvertisement) -> AdvertisementAPI | JSONResponse:
        try:
            adv = self.db.create(adv_request)
            response = self.db.get(adv)
            return AdvertisementAPI(**response.model_dump())
        except:
            raise CustomException(status_code=400, detail="Not created")

    def update_advertisement(self, adv_id: str, adv_request: UpdateAdvertisement) -> JSONResponse:
        adv = self.db.update(adv_id, adv_request)
        response = self.db.get(adv)
        return AdvertisementAPI(**response.model_dump())

    def delete_advertisement(self, adv_id: str) -> JSONResponse:
        return self.db.delete(adv_id)