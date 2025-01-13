from fastapi import APIRouter, Request, Depends
from app.models.v1.api.advertisements import UpdateAdvertisement, CreateAdvertisement
from app.database import get_database
from app.domain.v1.advertisements import Advertisement as AdvertisementDomain
from typing import List
from app.models.v1.api.advertisements import AdvertisementAPI
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/all_list", response_model=List[AdvertisementAPI])
async def get_list(db = Depends(get_database)) -> List[AdvertisementAPI]:
    domain = AdvertisementDomain(db)
    return domain.get_advertisements()


@router.get("/get/{adv_id}", response_model=AdvertisementAPI)
async def get(adv_id: str, db = Depends(get_database)) -> AdvertisementAPI | JSONResponse:
    domain = AdvertisementDomain(db)
    return domain.get_advertisement(adv_id)


@router.post("/create", response_model=str)
async def create(adv_request: CreateAdvertisement, db = Depends(get_database)) -> str | JSONResponse:
    domain = AdvertisementDomain(db)
    return domain.create_advertisement(adv_request)


@router.patch("/update/{adv_id}")
async def update(adv_id: str, adv_request: UpdateAdvertisement, db = Depends(get_database)) -> JSONResponse:
    domain = AdvertisementDomain(db)
    return domain.update_advertisement(adv_id, adv_request)

    
@router.delete("/delete/{adv_id}")
async def delete(adv_id: str, db = Depends(get_database)) -> JSONResponse:
    domain = AdvertisementDomain(db)
    return domain.delete_advertisement(adv_id)