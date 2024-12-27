from typing import Optional
from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field


class AdvertisementBase(BaseModel):
    title: str = Field(...)
    description: Optional[str]
    is_active: bool = Field(..., default=True)
    owner_id: int = Field(..., gt=0)