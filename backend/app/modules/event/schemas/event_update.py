from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from ..models import EventStatus

class EventSpeakerUpdate(BaseModel):
    speakers_to_delete: Optional[List[int]] = None
    speakers_to_connect: Optional[List[int]] = None

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[EventStatus] = None
    irl_meeting_space: Optional[str] = None
    online_meeting_space: Optional[str] = None
    stream_link: Optional[str] = None
    cover_url: Optional[str] = None
    registration_link: Optional[str] = None
    speakers: Optional[EventSpeakerUpdate] = None