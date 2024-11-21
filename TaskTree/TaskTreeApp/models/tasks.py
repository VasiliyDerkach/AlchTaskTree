
from ..backend.db import Base, engine
from sqlalchemy import Column, Text, Date
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import *
import uuid
class Tasks(Base):
    """
        Модуль models.tasks.py
        Задает модель таблицы Tasks
        поля Текст задачи (title),
        Дата начала выполнения задачи Start,
        Дата завершения задачи End.
        ключевое поле id - 36 значная строка формата uuid
    """
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    # _query_cls = Query
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(Text)
    start =  Column(Date)
    end =  Column(Date)
Base.metadata.create_all(engine,tables=[Tasks.__table__])