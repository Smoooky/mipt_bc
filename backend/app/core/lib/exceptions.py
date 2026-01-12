from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..logging.logger import logger
from .ApiError import ApiError

def handle_exception(e: Exception, context: dict = None):
    """
    Универсальный обработчик ошибок.
    context - словарь с ключевой информацией, например {"event_id": 42, "user_id": 5}
    """
    extra_data = context or {}

    if isinstance(e, ApiError):
        extra_data.update({
            "error_type": type(e).__name__,
            "message": e.message,
            "status_code": e.status_code,
        })

        logger.warning("Application error", extra_data=extra_data)

        raise HTTPException(
            status_code=e.status_code,
            detail=e.message
        )

    if isinstance(e, SQLAlchemyError):
        extra_data.update({
            "error_type": type(e).__name__,
            "message": str(e.__cause__ or e), 
        })
        logger.error("Database error occurred", extra_data=extra_data)

        if isinstance(e, IntegrityError):
            detail = "Violation of database restrictions"
            status_code = 400
        else: 
            detail = "Database internal error"
            status_code = 500
    
    elif isinstance(e, HTTPException):
        extra_data.update({"status_code": e.status_code, "detail": e.detail})
        logger.error("HTTP exception occurred", extra_data=extra_data)
        raise e

    else:
        # Любая непредвиденная ошибка
        extra_data.update({"error_type": type(e).__name__})
        logger.error("Unexpected error", extra_data=extra_data)
        detail = "Internal server error"
        status_code = 500
    
    raise HTTPException(status_code=status_code, detail=detail)