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
    start_date: datetime
    end_date: Optional[datetime] = None
    status: EventStatus
    irl_meeting_space: Optional[str] = None
    online_meeting_space: Optional[str] = None
    stream_link: Optional[str] = None
    cover_url: Optional[str] = None
    registration_link: str

    speakers: Optional[List[SpeakerResponse]] = None

    model_config = {
        "from_attributes": True
    }