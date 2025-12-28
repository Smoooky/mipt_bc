from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.modules.event.models.event import eventStatus
from app.modules.event.schemas.speakerResponse import speakerResponse

class eventResponse(BaseModel):
    """
    Схема полной модели события
    """
    id: int
    title: str
    description: str
    startDate: datetime
    endDate: Optional[datetime] = None
    status: eventStatus
    irlMeetingSpace: Optional[str] = None
    onlineMeetingSpace: Optional[str] = None
    streamLink: Optional[str] = None
    coverUrl: Optional[str] = None
    registrationLink: str

    speakers: List[speakerResponse] = []

    model_config = {
        "from_attributes": True
    }