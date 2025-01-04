from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from datetime import datetime
from app.v1.models.base.advertisements import Advertisement


class AdvertisementAPI(Advertisement):
    pass