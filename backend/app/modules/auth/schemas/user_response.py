from pydantic import BaseModel
from ..models import UserRole

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    tech_role: UserRole
    club_role: str

    model_config = {
        "from_attributes": True,
        "json_encoders": {
            UserRole: lambda v: v.value  # Enum -> str
        }
    }