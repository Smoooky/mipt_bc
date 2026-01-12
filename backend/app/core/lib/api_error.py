class ApiError(Exception):
    status_code = 500
    message = 'Internal error'

    def __init__(self, message: str | None = None):
        if message:
            self.message = message
        super().__init__(self.message)

class _BadRequest(ApiError):
    status_code = 400
    message = 'Bad request'

class _NotFound(ApiError):
    status_code = 404
    message = 'Not found'

class _Conflict(ApiError):
    status_code = 409
    message = 'Conflict'

class _Unauthorized(ApiError):
    status_code = 401
    message = 'Unauthorized'

class _Forbidden(ApiError):
    status_code = 403
    message = 'Forbidden'

class ApiErrors:
    BadRequest = _BadRequest
    NotFound = _NotFound
    Conflict = _Conflict
    Unauthorized = _Unauthorized
    Forbidden = _Forbidden