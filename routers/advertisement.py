from fastapi import APIRouter, HTTPException
from database import database
from pydantic import BaseModel
from models.advertisement import Advertisement
from bson import ObjectId
import datetime

router = APIRouter(
    prefix='/advertisement',
    tags=['advertisement'])

advertisements_collection = database['advertisements']

class AdvertisementRequest(BaseModel):
    title: str
    description: str
    owner_id: int


@router.get('/all_advertisements')
async def get_advertisements(d):
    advertisements_collection = database['advertisements']
    advertisements = advertisements_collection.find()
    
    advertisement_list = []
    for advertisement in advertisements:
        advertisement['_id'] = str(advertisement['_id'])
        advertisement_list.append(advertisement)
    
    return advertisement_list


@router.get('/{advertisement_id}')
async def get_advertisement(advertisement_id: str):
    try:
        advertisement_id = ObjectId(advertisement_id)  # Convert string to ObjectId
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid advertisement ID format")
    
    advertisement = advertisements_collection.find_one({"_id": advertisement_id})
    
    if not advertisement:
        raise HTTPException(status_code=404, detail='Not found')
    
    advertisement['_id'] = str(advertisement['_id'])  # Convert _id to string for the response
    return advertisement


@router.post('/create')
async def create_advertisement(advertisement_request: AdvertisementRequest):
    advertisement_model = Advertisement(
        title=advertisement_request.title,
        description=advertisement_request.description,
        owner_id=advertisement_request.owner_id,
    )

    advertisement_dict = {
        "title": advertisement_model.title,
        "description": advertisement_model.description,
        "modified_at": advertisement_model.modified_at,
        "created_at": advertisement_model.created_at,
        "owner_id": advertisement_model.owner_id,
    }
    
    result = advertisements_collection.insert_one(advertisement_dict)

    return {
        "message": "Advertisement  successfully!",
        "advertisement_id": str(result.inserted_id)
    }


@router.put('/update/{advertisement_id}')
async def update_advertisement(advertisement_id: str, advertisement_request: AdvertisementRequest):
    # Find the advertisement by its ID
    advertisement = advertisements_collection.find_one({"_id": ObjectId(advertisement_id)})

    if not advertisement:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    # Prepare updated advertisement data
    update_data = {
        "title": advertisement_request.title,
        "description": advertisement_request.description,
        "owner_id": advertisement_request.owner_id,
        "modified_at": datetime.datetime.utcnow()  # Set modified_at to the current time
    }

    # Update the advertisement
    result = advertisements_collection.update_one(
        {"_id": ObjectId(advertisement_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    return {
        "message": "Advertisement updated successfully!",
        "advertisement_id": advertisement_id
    }