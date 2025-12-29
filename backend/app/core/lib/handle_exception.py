from fastapi import HTTPException
from app.core.lib.CustomHTTPException import CustomHTTPException
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

        logger.warn("Application error", extra_data=extra_data)

        raise CustomHTTPException(
            status_code=e.status_code,
            detail=e.message,
            error_code=context['error_code'],
            additional_info=context.get("additional_info")
        )

    if isinstance(e, SQLAlchemyError):
        extra_data.update({
            "error_type": type(e).__name__,
            "message": str(e.__cause__ or e), 
            "detail": str(e._message or 'none')
        })
        logger.error("Database error occurred", extra_data=extra_data)

        if isinstance(e, IntegrityError):
            detail = "Violation of database restrictions"
            status_code = 400
        else: 
            detail = "Database internal error"
            status_code = 500

    else:
        # Любая непредвиденная ошибка
        extra_data.update({"error_type": type(e).__name__})
        logger.error("Unexpected error", extra_data=extra_data)
        detail = "Internal server error"
        status_code = 500
    
    raise CustomHTTPException(status_code=status_code, detail=detail)