from pydantic import BaseModel
from datetime import date


class Advertisement(BaseModel):
    title: str
    description: str    
    is_active: bool
    owner_id: int
    created_at: date