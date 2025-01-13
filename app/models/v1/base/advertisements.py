from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class Advertisement(BaseModel):
    title: str = Field(...)
    description: Optional[str] = Field(default=None)
    owner_id: str = Field(...)