from pydantic import BaseModel
from typing import Optional

class SpeakerResponse(BaseModel):
    id: int
    fullName: str
    bio: Optional[str] = None
    position: str
    company: str
    photoURL: Optional[str] = None

    model_config = {
        "from_attributes": True
    }