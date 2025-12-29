from fastapi import HTTPException
from typing import Any, Dict, Optional

class CustomHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None,
            headers: Optional[Dict[str, str]] = None,
            error_code: Optional[str] = None,
            additional_info: Optional[Dict] = None
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.error_code = error_code
        self.additional_info = additional_info
