from abc import ABC

from pydantic import BaseModel


class BaseEntity(ABC, BaseModel):
    """Базовая модель для сущностей."""
