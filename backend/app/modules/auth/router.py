from fastapi import APIRouter, Depends, status, Response, Request, Cookie, Header
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import AuthResponse, RegisterUserPayload, LoginUserPayload, InviteTokenData
from app.core.database import get_session
from app.core.lib import CustomHTTPException
from .service import AuthService
from datetime import datetime, timezone

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post(
    '/registration/{token}',
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    token: str,
    payload: RegisterUserPayload,
    response: Response,
    session: AsyncSession = Depends(get_session),
):
    service = AuthService(session)
    auth_data = await service.register_user(payload, token)
    max_age = int((auth_data.refresh_token.expires_at - datetime.now(timezone.utc)).total_seconds())
    response.headers['Authorization'] = f'Bearer {auth_data.access_token}'
    response.set_cookie(
        key='refresh_token',
        value=auth_data.refresh_token.token,
        httponly=True,
        secure=False, # Пока что
        samesite='strict',
        expires=max_age
    )
    return auth_data.user

@router.post(
    '/login',
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK
)
async def login_user(
    payload: LoginUserPayload,
    response: Response,
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)
    auth_data = await service.login_user(payload)
    max_age = int((auth_data.refresh_token.expires_at - datetime.now(timezone.utc)).total_seconds())
    response.headers['Authorization'] = f'Bearer {auth_data.access_token}'
    response.set_cookie(
        key='refresh_token',
        value=auth_data.refresh_token.token,
        httponly=True,
        secure=False, # Пока что
        samesite='strict',
        expires=max_age
    )
    return 

@router.post(
    '/logout',
    status_code=status.HTTP_200_OK
)
async def logout_user(
    response: Response,
    refresh_token: str = Cookie(alias='refresh_token'),
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)
    await service.logout_user(refresh_token)

    response.headers['Authorization'] = ''
    response.delete_cookie(key='refresh_token')
    return

@router.post(
    '/invite',
    response_model=str,
    status_code=status.HTTP_200_OK
)
async def create_invite(
    payload: InviteTokenData,
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)
    return await service.create_invite(payload)

@router.post(
    '/refresh',
    status_code=status.HTTP_200_OK
)
async def refresh_tokens(
    response: Response,
    refresh_token: str = Cookie(alias='refresh_token'),
    session: AsyncSession = Depends(get_session)
):
    if not refresh_token:
        raise CustomHTTPException(401, detail='Invalid refresh_token cookie')

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
    return
