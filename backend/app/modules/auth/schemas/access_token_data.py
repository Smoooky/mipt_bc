from pydantic import BaseModel
from .access_token_payload import AccessTokenPayload

class AccessTokenData(BaseModel):
    token: str
    user_data: AccessTokenPayload