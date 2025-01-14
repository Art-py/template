import uvicorn
from fastapi import FastAPI

from backend.core.exceptions import CustomException, custom_exception_handler, global_exception_handler
from backend.routers import test_rout


app = FastAPI()

app.include_router(test_rout.router, prefix="/api")

app.add_exception_handler(CustomException, custom_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


if __name__ == '__main__':
    uvicorn.run('backend.main:app')
