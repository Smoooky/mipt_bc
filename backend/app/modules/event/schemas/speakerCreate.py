from pydantic import BaseModel
from typing import Optional

class speakerCreate(BaseModel):
    fullName: str
    bio: Optional[str] = None
    position: str
    company: str
    photoURL: Optional[str] = None