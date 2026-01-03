from datetime import datetime, timezone, timedelta
from jose import jwt
import secrets
from app.core import settings
from ..schemas import AccessTokenData, InviteTokenData, RefreshTokenData

def generate_access_token(data: AccessTokenData) -> str:
    to_encode = data.model_dump()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_access_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_access_token

def decode_access_token(token: str) -> AccessTokenData:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return AccessTokenData(**payload)

def generate_refresh_token() -> RefreshTokenData:
    token = secrets.token_urlsafe(48)
    expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return RefreshTokenData(token=token, expires_at=expires_at)

def generate_invite_token(data: InviteTokenData) -> str:
    to_encode = data.model_dump()
    expire = datetime.now(timezone.utc) + timedelta(hours=data.expires_in)
    to_encode.update({"exp": expire})
    encoded_invite_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_invite_token

def decode_invite_token(token: str) -> InviteTokenData:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return InviteTokenData(**payload)