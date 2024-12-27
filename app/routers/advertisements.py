from fastapi import APIRouter
from app.crud import get_datas, get_data, create_data, update_data, delete_data

router = APIRouter()


@router.get("/all_advertisements/")
async def get_advertisements():
    return await get_datas()


@router.get("/get_advertisement/{adv_id}")
async def get_advertisements(adv_id: int):
    return await get_data(adv_id)


@router.post("/create_advertisement")
async def create_advertisement():
    return await create_data()


@router.put("/update_advertisement/{adv_id}")
async def update_advertisement(adv_id: int):
    return await update_data(adv_id)

    
@router.delete("/delete_advertisement/{adv_id}")
async def delete_advertisement(adv_id: int):
    return await delete_data(adv_id)