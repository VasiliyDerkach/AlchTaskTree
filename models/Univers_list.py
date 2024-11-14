from backend.db import Base
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
class Univers_list(Base):
    __tablename__ = 'univers_list'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    id_out =Column(String)
    id_in = Column(String)
    num_in_link = Column(Integer)
    role = Column(String)
