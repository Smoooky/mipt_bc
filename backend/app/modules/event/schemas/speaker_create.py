from pydantic import BaseModel
from typing import Optional

class SpeakerCreate(BaseModel):
    full_name: str
    bio: Optional[str] = None
    position: str
    company: str
    photo_url: Optional[str] = None