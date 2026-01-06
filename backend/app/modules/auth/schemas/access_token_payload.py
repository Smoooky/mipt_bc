from pydantic import BaseModel
from ..models import UserRole

class AccessTokenPayload(BaseModel):
    id: int
    role: UserRole