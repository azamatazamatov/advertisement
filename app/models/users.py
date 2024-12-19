from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    username: str
    full_name: str
    phone_number: str
    hashed_password: str
    is_active: bool
    created_at: date