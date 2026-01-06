from pydantic import BaseModel
from typing import Optional

class SpeakerResponse(BaseModel):
    id: int
    full_name: str
    bio: Optional[str] = None
    position: str
    company: str
    photo_url: Optional[str] = None

    model_config = {
        "from_attributes": True
    }