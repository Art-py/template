from fastapi import APIRouter


router = APIRouter()


@router.get(path="/hello/", summary='Говорит привет миру', tags=['Тестовый ендпоинт'])
async def sad_hello():
    data = {'Hello!': 'Hello world!'}
    return data
