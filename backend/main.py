import uvicorn
from fastapi import FastAPI
from backend.routers import test_rout


app = FastAPI()

app.include_router(test_rout.router, prefix="/api")


if __name__ == '__main__':
    uvicorn.run('backend.main:app')
