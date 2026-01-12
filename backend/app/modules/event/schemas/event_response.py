from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.modules.event.models.event import EventStatus
from app.modules.event.schemas.speaker_response import SpeakerResponse

class EventResponse(BaseModel):
    """
    Схема полной модели события
    """
    id: int
    title: str
    description: str
    startDate: datetime
    endDate: Optional[datetime] = None
    status: EventStatus
    irlMeetingSpace: Optional[str] = None
    onlineMeetingSpace: Optional[str] = None
    streamLink: Optional[str] = None
    coverUrl: Optional[str] = None
    registrationLink: str

    speakers: List[SpeakerResponse] = []

    model_config = {
        "from_attributes": True
    }