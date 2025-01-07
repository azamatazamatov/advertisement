from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


def validate_objectid(value: str):
    try:
        return ObjectId(value)
    except:
        raise ValueError("Invalid ObjectId")

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield validate_objectid
        
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Advertisement(BaseModel):
    id: PyObjectId = Field(..., alias='_id')
    title: str = Field(...)
    description: Optional[str] = Field(default=None)
    owner_id: str = Field(...)
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # convert ObjectId to string
        }