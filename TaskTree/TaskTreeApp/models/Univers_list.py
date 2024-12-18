from ..backend.db import engine, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

class Univers_list(Base):
    """
        Модуль models.Universal_list.py

        Модель таблицы Univers_list
        для связывание задач между собой и контактами.
        созаваемое автоматически целочисленное поле id - ключевое поле для определения уникального указателя на запись таблицы,
        используемое для удаления и редактирования данных талицы.
        id_out - текстовое поле для хранения указателя на id задачи (в формате uuid), от которой исходит взаимсвязь
         с другой задачей или с констактом (исходящая стрелка).
        id_in - текстовое поле для хранения указателя на id задачи или контакта (в формате uuid), в которую входит взаимсвязь
         с другой задачей (входящая стрелка).
         Role - текстовое поле для хранения данных о характере взаимосвязи задачи и контакта (исполнитель, контролер и т.п.).
         Для взаимосвязи задач значение по умолчанию 'arrow'.
         num_in_link - целочисленное поле для автоматической нумерации записей таблицы взаимсвязей для задачи с id=id_out
         (нумерация исходящих стрелок для одной задачи).
         Для взаимсвязи задач и конктактов   num_in_link=0
         Поле предназначено для расшрения функционала приложения в будущем. Например, сложный алгоритм определния актуальности
         задачи по входящим в нее нумерованным стрелкам по типу Arrow[1] and (Arrow[2] or Arrow[3])
    """
    __tablename__ = 'Univers_list'
    __table_args__ = {'keep_existing': True}
    id_num = Column(Integer, primary_key=True, index=True)
    id_out =Column(UUID(as_uuid=True))
    id_in = Column(UUID(as_uuid=True))
    num_in_link = Column(Integer)
    role = Column(String)

Base.metadata.create_all(engine,tables=[Univers_list.__table__])
