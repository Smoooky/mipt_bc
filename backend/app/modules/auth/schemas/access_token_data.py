from pydantic import BaseModel
from ..models import UserRole

class AccessTokenData(BaseModel):
    id: int
    role: UserRole