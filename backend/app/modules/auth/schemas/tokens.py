from pydantic import BaseModel
from .refresh_token_data import RefreshTokenData
from .access_token_data import AccessTokenData

class Tokens(BaseModel):
    access_token: AccessTokenData
    refresh_token: RefreshTokenData