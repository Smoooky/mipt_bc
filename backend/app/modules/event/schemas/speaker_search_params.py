from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SpeakerSearchParams(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    position: Optional[str] = None
    company: Optional[str] = None