from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Advertisement(BaseModel):
    title: str = Field(...)
    description: Optional[str] = Field(default=None)
    owner_id: str = Field(...)