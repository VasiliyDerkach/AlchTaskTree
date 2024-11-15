from backend.db import engine, Base
from sqlalchemy import Column, Text, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import *
# from sqlalchemy import *
import uuid


class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(Text)
    start =  Column(Date)
    end =  Column(Date)

# from sqlalchemy.schema import CreateTable
# CreateTable(Tasks.__table__)
Base.metadata.create_all(engine,tables=[Tasks.__table__])