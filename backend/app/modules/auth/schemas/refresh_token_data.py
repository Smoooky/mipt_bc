from pydantic import BaseModel
from datetime import datetime

class RefreshTokenData(BaseModel):
    token: str
    expires_at: datetime