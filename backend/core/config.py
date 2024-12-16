import os
from typing import ClassVar

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user: ClassVar[str] = os.getenv('POSTGRES_USER', 'postgres_admin')
    password: ClassVar[str] = os.getenv('POSTGRES_PASSWORD', 'postgres_admin_123')
    db: ClassVar[str] = os.getenv('POSTGRES_DB', 'postgres_templates')

    APP_NAME: str = os.getenv('APP_NAME', 'Test_project')
    DATABASE_URL: str = f'postgresql+asyncpg://{user}:{password}@localhost:5432/{db}'


    class Config:
        env_file = '.env'


settings = Settings()
