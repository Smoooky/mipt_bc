from pydantic import BaseModel
from typing import Optional
from ..models import EventStatus
from datetime import datetime

class EventSearchParams(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[EventStatus] = None
    start_date_from: Optional[datetime] = None
    start_date_to: Optional[datetime] = None
    end_date_from: Optional[datetime] = None
    end_date_to: Optional[datetime] = None
    irl_meeting_space: Optional[str] = None
    online_meeting_space: Optional[str] = None