from typing import Optional
from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.base import AdvertisementBase


class AdvertisementDB(AdvertisementBase):
    id: int = Field(...)
    created_at: datetime = datetime.now()