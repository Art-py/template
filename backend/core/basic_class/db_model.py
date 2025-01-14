from uuid6 import uuid7
from sqlalchemy import MetaData, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseDBModel(AsyncAttrs, DeclarativeBase):
    """Базовый класс моделей SQLAlchemy с поддержкой UUIDv7 и naming conventions."""

    convention = {
        'ix': 'ix_%(table_name)s_%(column_0_N_name)s',
        'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
        'fk': 'fk_%(table_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    }
    metadata = MetaData(naming_convention=convention)

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid7,
        index=True,
    )
