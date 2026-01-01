from pydantic import BaseModel
from .user_response import UserResponse

class AuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str