from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from app.models.v1.base.advertisements import Advertisement
from bson.objectid import ObjectId


class AdvertisementDB(Advertisement):
    id: ObjectId = Field(..., alias="_id")
    is_active: bool = Field(default=True)
    created_at: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True

    @field_validator("id")
    @classmethod
    def transform(cls, id: ObjectId):
        return str(id)

