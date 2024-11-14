from backend.db import Base
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
class Contacts(Base):
    __tablename__ = 'contacts'
    __table_args__ = {'keep_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    last_name = Column(String)
    first_name = Column(String)
    second_name = Column(String)
