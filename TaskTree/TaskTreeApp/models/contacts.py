
from ..backend.db import engine, Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Contacts(Base):
    """
        Модуль models.contacts.py

        Модель таблицы Контакты (Contacts).
        поля Фамилия - last_name, Имя - first_name, Отчество - second_name.
        ключевое поле id - 36 значная строка формата uuid
    """
    __tablename__ = 'contacts'
    __table_args__ = {'keep_existing': True}
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    last_name = Column(String)
    first_name = Column(String)
    second_name = Column(String)

Base.metadata.create_all(engine,tables=[Contacts.__table__])