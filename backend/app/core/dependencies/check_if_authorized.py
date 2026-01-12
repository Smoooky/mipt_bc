from fastapi import Header, Cookie, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.auth.utils import decode_access_token
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import AccessTokenPayload
from app.core.database import get_session
from app.core.lib import CustomHTTPException
from app.core.logging import logger

async def check_if_authorized(
        response: Response,
        authorization: str = Header(alias='Authorization'),
        refresh_token: str = Cookie(alias='refresh_token'),
        session: AsyncSession = Depends(get_session)
) -> AccessTokenPayload:
    """
    Docstring for check_if_authorized
    
    :return: User data from access token
    :rtype: AccessTokenPayload
    """
    if not authorization.startswith('Bearer '):
        raise CustomHTTPException(status_code=401, detail='Invalid authorization header')
    
    access_token = authorization.removeprefix('Bearer ').strip()

    try:
        user_data = decode_access_token(access_token)
        return user_data
    except Exception:
        logger.warn(msg='Invalid or expired access token. Trying to update')

        if not refresh_token:
            raise CustomHTTPException(status_code=401, detail='Access expired and no refresh token')

        service = AuthService(session)

        refresh_data = await service.refresh_tokens(refresh_token)

        response.headers['Authorization'] = f'Bearer {refresh_data.access_token}'
        response.set_cookie(
            key='refresh_token',
            value=refresh_data.refresh_token.token,
            httponly=True,
            secure=False, # Пока что
            samesite='strict',
            expires=refresh_data.refresh_token.expires_at
        )
        return refresh_data.access_token.user_data