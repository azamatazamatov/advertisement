from fastapi import APIRouter, Request, Depends
from app.crud.v1.advertisements import AdvertisementCRUD
from app.database import get_database
from app.models.v1.api.advertisements import UpdateAdvertisement, CreateAdvertisement

router = APIRouter()

@router.get("/all_list")
async def get_list( db = Depends(get_database)):
    db = AdvertisementCRUD(db)
    return db.get_list()


@router.get("/get/{adv_id}")
async def get(adv_id: str, db = Depends(get_database)):
    db = AdvertisementCRUD(db)
    return db.get(adv_id)


@router.post("/create")
async def create(adv_request: CreateAdvertisement, db = Depends(get_database)):
    db = AdvertisementCRUD(db)
    return db.create(adv_request)


@router.patch("/update/{adv_id}")
async def update(adv_id: str, adv_request: UpdateAdvertisement, db = Depends(get_database)):
    db = AdvertisementCRUD(db)
    return db.update(adv_id, adv_request)

    
@router.delete("/delete/{adv_id}")
async def delete(adv_id: str, db = Depends(get_database)):
    db = AdvertisementCRUD(db)
    return db.delete(adv_id)