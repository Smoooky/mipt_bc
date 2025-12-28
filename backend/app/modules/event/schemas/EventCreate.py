from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from ..models import EventStatus

class eventCreate(BaseModel):
    title: str
    description: str
    startDate: datetime
    endDate: Optional[datetime] = None
    status: Optional[EventStatus] = EventStatus.FUTURE
    irlMeetingSpace: Optional[str] = None
    onlineMeetingSpace: Optional[str] = None
    streamLink: Optional[str] = None
    coverUrl: Optional[str] = None
    registrationLink: str
    speakerIds: Optional[List[int]] = [] 