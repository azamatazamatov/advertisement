from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.v1.base.advertisements import Advertisement


class AdvertisementDB(Advertisement):
    is_active: bool = Field(default=True)
    created_at: datetime = datetime.now()