from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str = Field(...)
    full_name: Optional[str]
    phone_number: Optional[str]
    hashed_password: str = Field(...)
    is_active: bool = Field(..., default=True)