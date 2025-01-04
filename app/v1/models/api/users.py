from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.v1.models.base.users import User

class UserAPI(User):
    pass