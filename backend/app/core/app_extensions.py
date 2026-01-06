from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.core.lib import CustomHTTPException

def register_extensions(app: FastAPI):
    # Custom exceptions
    @app.exception_handler(CustomHTTPException)
    async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "detail": exc.detail,
                    "error_code": exc.error_code,
                    "addition_info": exc.additional_info,
                    "status_code": exc.status_code
                }
            }
        )