from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import AuthResponse, RegisterUserPayload, LoginUserPayload, InviteTokenData
from app.core.database import get_session
from .service import AuthService

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
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)
    return await service.register_user(payload, token)

@router.post(
    '/login',
    response_model=AuthResponse,
    status_code=status.HTTP_200_OK
)
async def login_user(
    payload: LoginUserPayload,
    session: AsyncSession = Depends(get_session)
):
    service = AuthService(session)
    return await service.login_user(payload)

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