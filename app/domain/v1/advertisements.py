from app.crud.v1.advertisements import Advertisement as AdvertisementCrud
from app.models.v1.api.advertisements import AdvertisementAPI
from app.models.v1.api.advertisements import UpdateAdvertisement, CreateAdvertisement
from pymongo.database import Database
from fastapi.responses import JSONResponse
from typing import List


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
            return JSONResponse(status_code=404, content='Not found')

    def create_advertisement(self, adv_request: CreateAdvertisement) -> str | JSONResponse:
        try:
            return self.db.create(adv_request)
        except:
            return JSONResponse(status_code=400, content='Not created')

    def update_advertisement(self, adv_id: str, adv_request: UpdateAdvertisement) -> JSONResponse:
        adv = self.db.update(adv_id, adv_request)
        return adv

    def delete_advertisement(self, adv_id: str) -> JSONResponse:
        return self.db.delete(adv_id)