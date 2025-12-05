from core.database.base_model import Base
from sqlalchemy import Column, Integer, TEXT, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone

class EventSpeaker(Base):
    __tablename__ = 'event_speakers'

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    speaker_id = Column(Integer, ForeignKey('speakers.id'), primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    event = relationship('Event', back_populates='speaker_links')
    speaker = relationship("Speaker", back_populates="event_links")