from pydantic import Field
from app.v1.models.base.users import User
from datetime import datetime
from bson.objectid import ObjectId

class UserDB(User):
    id: ObjectId = Field(...)
    hashed_password: str = Field(...)
    is_active: bool = Field(..., default=True)
    created_at: datetime = datetime.now()