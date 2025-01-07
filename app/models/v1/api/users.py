from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.v1.base.users import User

class UserAPI(User):
    pass