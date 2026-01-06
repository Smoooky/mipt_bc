from pydantic import BaseModel
from ..models import UserRole
from typing import Optional

class InviteTokenData(BaseModel):
    sender_id: Optional[int] = None 
    role: Optional[UserRole] = None
    expires_in: int # Количество часов