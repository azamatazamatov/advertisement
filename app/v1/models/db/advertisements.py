from typing import Optional
from bson.objectid import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field
from app.v1.models.base.advertisements import Advertisement


class AdvertisementDB(Advertisement):
    id: ObjectId = Field(...)
    is_active: bool = Field(..., default=True)
    created_at: datetime = datetime.now()