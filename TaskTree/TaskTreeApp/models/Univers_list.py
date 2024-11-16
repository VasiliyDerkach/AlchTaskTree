from ..backend.db import engine, Base
from sqlalchemy import Column, Integer, String


class Univers_list(Base):
    __tablename__ = 'univers_list'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    id_out =Column(String)
    id_in = Column(String)
    num_in_link = Column(Integer)
    role = Column(String)

# from sqlalchemy.schema import CreateTable
# CreateTable(Univers_list.__table__)
# Base.metadata.create_all(engine)
Base.metadata.create_all(engine,tables=[Univers_list.__table__])
