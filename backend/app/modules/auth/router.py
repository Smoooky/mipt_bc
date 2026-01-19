from fastapi import APIRouter, Depends, status, Response, Request, Cookie, Header
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import AuthResponse, LoginUserPayload, InviteTokenData, RegisterUserPayload, UserResponse, UpdateRolePayload
from .models import UserRole
from app.core.database.session import get_session
from app.core.lib import CustomHTTPException
from app.core.dependencies import role_required_factory
from .service import AuthService
from datetime import datetime, timezone

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post(
    '/registration/{token}',
    response_model=UserResponse,
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

    response.headers['Authorization'] = f'Bearer {auth_data.access_token.token}'
    response.set_cookie(
        key='refresh_token',
        value=auth_data.refresh_token.token,
        httponly=True,
        secure=False, # Пока что
        samesite='strict',
        expires=auth_data.refresh_token.expires_at
    )
    return auth_data.user

@router.post(
    '/login',
    status_code=status.HTTP_204_NO_CONTENT
)
async def login_user(
    payload: LoginUserPayload,
    response: Response,
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)

    auth_data = await service.login_user(payload)

    response.headers['Authorization'] = f'Bearer {auth_data.access_token.token}'
    response.set_cookie(
        key='refresh_token',
        value=auth_data.refresh_token.token,
        httponly=True,
        secure=False, # Пока что
        samesite='strict',
        expires=auth_data.refresh_token.expires_at
    )
    return 

@router.post(
    '/logout',
    status_code=status.HTTP_204_NO_CONTENT
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

    response.headers['Authorization'] = f'Bearer {refresh_data.access_token.token}'
    response.set_cookie(
        key='refresh_token',
        value=refresh_data.refresh_token.token,
        httponly=True,
        secure=False, # Пока что
        samesite='strict',
        expires=refresh_data.refresh_token.expires_at
    )
    return

@router.patch(
    '/admin/role',
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_role(
    payload: UpdateRolePayload,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(UserRole.ADMIN))
):
    service = AuthService(session)
    await service.update_role(
        user_id=payload.user_id,
        role=payload.role
    )
    return