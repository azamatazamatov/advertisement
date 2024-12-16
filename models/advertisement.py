from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Advertisement(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    modified_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())
    owner_id = Column(Integer, ForeignKey('users.id'))