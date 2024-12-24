import os

from pydantic_settings import BaseSettings

USER: str = os.getenv('POSTGRES_USER', 'postgres_admin')
PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'postgres_admin_123')
DB: str = os.getenv('POSTGRES_DB', 'postgres_templates')


class Settings(BaseSettings):
    APP_NAME: str = os.getenv('APP_NAME', 'Test_project')
    DATABASE_URL: str = f'postgresql+asyncpg://{USER}:{PASSWORD}@localhost:5432/{DB}'

    class Config:
        env_file = '.env'


settings = Settings()
