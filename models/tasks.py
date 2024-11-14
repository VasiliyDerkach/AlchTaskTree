from backend.db import Base
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(Text)
    start =  Column(Date)
    end =  Column(Date)