from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db.database import get_db


router = APIRouter()


@router.get("/hello/")
async def sad_hello(db: AsyncSession = Depends(get_db)):
    data = {'Hello!': 'Hello world!'}
    return data
