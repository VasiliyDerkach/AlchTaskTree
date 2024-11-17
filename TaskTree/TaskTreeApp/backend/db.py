from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey
# from models import *
engine = create_engine('sqlite:///db.sqlite3.db',echo=True)
SessionLocal = sessionmaker(bind=engine)
DBSession = Session(engine)
class Base(DeclarativeBase):
    pass

# Base.metadata.create_all(engine)
