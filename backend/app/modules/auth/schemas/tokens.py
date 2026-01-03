from pydantic import BaseModel
from .refresh_token_data import RefreshTokenData

class Tokens(BaseModel):
    access_token: str
    refresh_token: RefreshTokenData