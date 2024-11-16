from ..backend.db import engine, Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Contacts(Base):
    __tablename__ = 'contacts'
    __table_args__ = {'keep_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    last_name = Column(String)
    first_name = Column(String)
    second_name = Column(String)

# from sqlalchemy.schema import CreateTable
# CreateTable(Contacts.__table__)
Base.metadata.create_all(engine,tables=[Contacts.__table__])