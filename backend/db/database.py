from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with async_session() as session:
        yield session
        