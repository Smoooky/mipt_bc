from pydantic import BaseModel
from ..models import UserRole

class UpdateRolePayload(BaseModel):
    user_id: int
    role: UserRole