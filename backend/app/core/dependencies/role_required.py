from fastapi import Depends
from app.core.lib import ApiErrors, handle_exception
from app.modules.auth import AccessTokenPayload
from .check_if_authorized import check_if_authorized

def role_required_factory(*roles):
    async def dependency(user_data: AccessTokenPayload = Depends(check_if_authorized)):
        try:
            if user_data.role not in roles:
                raise ApiErrors.Forbidden()
            return user_data
        except Exception as e:
            handle_exception(e, context={"error_code": "FORBIDDEN"})
    return dependency