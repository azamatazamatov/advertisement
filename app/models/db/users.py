from pydantic import Field
from app.models.base import UserBase
from datetime import datetime

class UserDB(UserBase):
    id: int = Field(...)
    created_at: datetime = datetime.now()