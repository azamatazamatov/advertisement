from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    username: str = Field(...)
    full_name: Optional[str]
    phone_number: Optional[int] = Field(default=None, gt=0)