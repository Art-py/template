from fastapi import FastAPI
from backend.routers import items


app = FastAPI()

app.include_router(items.router, prefix="/api")
