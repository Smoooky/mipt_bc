from pydantic import BaseModel
from typing import Optional

class SpeakerUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    position: Optional[str] = None
    company: Optional[str] = None
    photo_url: Optional[str] = None