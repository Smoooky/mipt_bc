from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import AuthResponse, RegisterUserPayload, UserResponse, LoginUserPayload, InviteTokenData, AccessTokenData
from .models import User, Invite
from app.core.logging import logger
from app.core.lib import handle_exception, ApiErrors
from .utils import hash_password, verify_password, generate_access_token, generate_invite_token, decode_invite_token
from datetime import datetime, timedelta, timezone
from app.core import settings

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.registration_page_url = settings.REGISTRATION_PAGE_URL
    
    async def register_user(self, data: RegisterUserPayload, invite_token: str) -> AuthResponse:
        # Проверка приглашения до работы с транзакцией
        invite = await self.session.scalar(
            select(Invite).where(Invite.token == invite_token)
        )
        if not invite:
            raise ApiErrors.Unauthorized('Invalid invite link')
        if invite.used_at:
            raise ApiErrors.Conflict('Invite link already used')
        if invite.expires_at and invite.expires_at < datetime.now(timezone.utc):
            raise ApiErrors.Conflict('Invite link expired')

        # Проверка существующего пользователя
        existence = await self.session.scalar(
            select(User).where(User.email == data.email)
        )
        if existence:
            raise ApiErrors.Conflict(f'User with email {data.email} already exists')

        try:
            # Добавляем пользователя и обновляем invite
            user = User(
                email=data.email,
                password_hash=hash_password(data.password),
                full_name=data.full_name,
                tech_role=invite.role
            )

            self.session.add(user)
            await self.session.flush()  # чтобы получить id пользователя

            invite.used_at = datetime.now(timezone.utc)
            invite.used_by_id = user.id
            self.session.add(invite)

            # если внешний код не оборачивает в begin(), можно здесь явно:
            # async with self.session.begin(): pass  # только если нужно

            access_token = generate_access_token(AccessTokenData(id=user.id, role=user.tech_role))

            return AuthResponse(
                user=UserResponse.model_validate(user),
                access_token=access_token,
                token_type='bearer'
            )

        except Exception as e:
            # Безопасно передаем контекст прямо в handle_exception
            handle_exception(
                e,
                context={
                    'error_code': 'USER_REGISTRATION_ERROR',
                    'user_email': data.email
                }
    )

    async def login_user(self, data: LoginUserPayload) -> AuthResponse:
        try:
            user = await self.session.scalar(
                select(User).where(User.email == data.email)
            )

            if not user:
                raise ApiErrors.Unauthorized(f'Invalid credentials. User with email {data.email} does not exists')
            
            if not verify_password(data.password, user.password_hash):
                raise ApiErrors.Unauthorized(f'Invalid credentials. Incorrect password')
            
            access_token = generate_access_token(
                user.id,
                user.tech_role
            )

            return AuthResponse(
                user=UserResponse.model_validate(user),
                access_token=access_token,
                token_type='bearer'
            )

        except Exception as e:
            handle_exception(
                e,
                context={
                    'error_code': 'USER_LOGIN_ERROR',
                    'user_email': data.email
                }
            )
    
    async def create_invite(self, link_in: InviteTokenData) -> str:
        try:
            token = generate_invite_token(link_in)
            invite = Invite(
                token=token,
                role=link_in.role,
                invited_by_id=link_in.sender_id,
                expires_at=datetime.now(timezone.utc) + timedelta(hours=link_in.expires_in)
            )

            async with self.session.begin():
                self.session.add(invite)
                await self.session.flush()

            return self.registration_page_url + invite.token

        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "REGISTRAION_LINK_GENERATE_ERROR"
                }
            )