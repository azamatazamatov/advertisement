from fastapi import APIRouter, Request
from app.v1.crud.advertisements import Advertisement
from app.v1.database import get_database
from app.v1.models.api.advertisements import AdvertisementAPI

router = APIRouter(
    prefix="/api/v1/advertisement",
    tags=["Advertisement"]
)

@router.get("/all_list")
async def get_list(request: Request):
    db = Advertisement(await get_database(request))
    return db.get_advertisements()


@router.get("/get/{adv_id}")
async def get(adv_id: str, request: Request):
    db = Advertisement(await get_database(request))
    return db.get_advertisement(adv_id)


@router.post("/create")
async def create(request: Request, adv_request: AdvertisementAPI):
    db = Advertisement(await get_database(request))
    return db.create_advertisement(adv_request)


@router.put("/update/{adv_id}")
async def update(adv_id: str, request: Request, adv_request: AdvertisementAPI):
    db = Advertisement(await get_database(request))
    return db.update_advertisement(adv_id, adv_request)

    
@router.delete("/delete/{adv_id}")
async def delete(adv_id: str, request: Request):
    db = Advertisement(await get_database(request))
    return db.delete_advertisement(adv_id)