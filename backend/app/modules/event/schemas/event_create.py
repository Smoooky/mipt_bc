from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from ..models import EventStatus

class EventCreate(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[EventStatus] = EventStatus.FUTURE
    irl_meeting_space: Optional[str] = None
    online_meeting_space: Optional[str] = None
    stream_link: Optional[str] = None
    cover_url: Optional[str] = None
    registration_link: str
    speaker_ids: Optional[List[int]] = [] 