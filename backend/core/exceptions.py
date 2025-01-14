from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


class CustomException(Exception):
    """Пользовательское исключение."""
    def __init__(self, name: str, detail: str):
        self.name = name
        self.detail = detail


async def custom_exception_handler(request: Request, exc: CustomException, status: int = 400):
    return JSONResponse(
        status_code=status,
        content={
            "error": exc.name,
            "message": exc.detail,
        },
    )


async def global_exception_handler(request: Request, exc: Exception, status: int = 500):
    return JSONResponse(
        status_code=status,
        content={
            "error": "Internal Server Error",
            "message": str(exc),
        },
    )
