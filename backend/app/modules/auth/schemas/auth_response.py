from pydantic import BaseModel
from .user_response import UserResponse
from .refresh_token_data import RefreshTokenData
from .access_token_data import AccessTokenData

class AuthResponse(BaseModel):
    user: UserResponse
    access_token: AccessTokenData
    refresh_token: RefreshTokenData