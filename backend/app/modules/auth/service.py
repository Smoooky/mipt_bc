from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from .schemas import AuthResponse, RegisterUserPayload, UserResponse, LoginUserPayload, InviteTokenData, AccessTokenData, Tokens
from .models import User, Invite, RefreshToken
from app.core.logging import logger
from app.core.lib import handle_exception, ApiErrors
from .utils import hash_password, verify_password, generate_access_token, generate_invite_token, generate_refresh_token, hash_refresh_token, decode_access_token
from datetime import datetime, timedelta, timezone
from app.core import settings

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.registration_page_url = settings.REGISTRATION_PAGE_URL
    
    async def register_user(self, data: RegisterUserPayload, invite_token: str) -> AuthResponse:
        try:
            invite = await self.session.scalar(
                select(Invite).where(Invite.token == invite_token)
            )
            if not invite:
                raise ApiErrors.Unauthorized('Invalid invite link')
            if invite.used_at:
                raise ApiErrors.Conflict('Invite link already used')
            if invite.expires_at and invite.expires_at < datetime.now(timezone.utc):
                raise ApiErrors.Conflict('Invite link expired')

            existence = await self.session.scalar(
                select(User).where(User.email == data.email)
            )
            if existence:
                raise ApiErrors.Conflict(f'User with email {data.email} already exists')

            user = User(
                email=data.email,
                password_hash=hash_password(data.password),
                full_name=data.full_name,
                tech_role=invite.role
            )

            self.session.add(user)
            await self.session.flush()

            invite.used_at = datetime.now(timezone.utc)
            invite.used_by_id = user.id
            self.session.add(invite)

            access_token = generate_access_token(AccessTokenData(id=user.id, role=user.tech_role))
            refresh_token_data = generate_refresh_token()

            refresh_token = RefreshToken(
                user_id = user.id,
                token_hash = hash_refresh_token(refresh_token_data.token),
                expires_at = refresh_token_data.expires_at
            )
            self.session.add(refresh_token)

            await self.session.commit()

            return AuthResponse(
                user=UserResponse.model_validate(user),
                access_token=access_token,
                refresh_token=refresh_token_data,
            )

        except Exception as e:
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
            
            access_token = generate_access_token(AccessTokenData(id=user.id, role=user.tech_role))
            refresh_token_data = generate_refresh_token()

            refresh_token = RefreshToken(
                user_id = user.id,
                token_hash = hash_refresh_token(refresh_token_data.token),
                expires_at = refresh_token_data.expires_at
            )
            self.session.add(refresh_token)

            await self.session.commit()

            return AuthResponse(
                user=UserResponse.model_validate(user),
                access_token=access_token,
                refresh_token=refresh_token_data,
            )

        except Exception as e:
            handle_exception(
                e,
                context={
                    'error_code': 'USER_LOGIN_ERROR',
                    'user_email': data.email
                }
            )

    async def logout_user(self, refresh_token: str) -> None:
        try:
            await self.session.execute(
                delete(RefreshToken).where(RefreshToken.token_hash == hash_refresh_token(refresh_token))
            )
            await self.session.commit()

            return

        except Exception as e:
            handle_exception(
                e,
                context={
                    'error_code': 'USER_LOGOUT_ERROR',
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

    async def refresh_tokens(self, refresh_token: str) -> Tokens:
        try:
            old_refresh_token = await self.session.scalar(
                select(RefreshToken).where(RefreshToken.token_hash == hash_refresh_token(refresh_token))
            )
            
            if not old_refresh_token:
                raise ApiErrors.Unauthorized(f'Invalid refresh token')
            if old_refresh_token.expires_at < datetime.now(timezone.utc):
                raise ApiErrors.Unauthorized(f'Refresh token expired')
            await self.session.execute(delete(RefreshToken).where(RefreshToken.id == old_refresh_token.id))

            user = await self.session.scalar(
                select(User).where(User.id == old_refresh_token.user_id)
            )

            if not user:
                raise ApiErrors.NotFound(f'User with id {old_refresh_token.user_id} not found')

            new_access_token = generate_access_token(AccessTokenData(id=user.id, role=user.tech_role))
            new_refresh_token = generate_refresh_token()

            self.session.add(
                RefreshToken(
                    user_id = old_refresh_token.user_id,
                    token_hash = hash_refresh_token(new_refresh_token.token),
                    expires_at = new_refresh_token.expires_at
                )
            )

            await self.session.commit()

            return Tokens(access_token=new_access_token, refresh_token=new_refresh_token)

        
        except Exception as e:
            handle_exception(
                e,
                context={
                    "error_code": "REFRESH_TOKENS_ERROR",
                }
            )