from pydantic import BaseModel
import datetime

class RefreshTokenData(BaseModel):
    token: str
    expires_at: datetime