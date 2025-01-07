from pydantic import Field, BaseModel
from app.models.v1.base.advertisements import Advertisement
from typing import Optional


class UpdateAdvertisement(BaseModel):
    title: str = Field(...)
    description: Optional[str] = Field(default=None)


class CreateAdvertisement(BaseModel):
    title: str = Field(...)
    description: Optional[str] = Field(default=None)
    owner_id: str = Field(...)

class AdvertisementAPI(Advertisement):
    pass