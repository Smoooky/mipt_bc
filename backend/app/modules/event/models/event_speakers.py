"""
Docstring for backend.app.modules.event.models.Event
Тут описывается модель для СВЯЗИ МЕРОПРИЯТИЯ И СПИКЕРА
"""
from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, TEXT, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone

class EventSpeaker(Base):
    __tablename__ = 'EventSpeakers'

    event_id = Column(Integer, ForeignKey('Events.id', ondelete='CASCADE'), primary_key=True)
    speaker_id = Column(Integer, ForeignKey('Speakers.id', ondelete='CASCADE'), primary_key=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    events = relationship('Event', back_populates='speaker_links')
    speakers = relationship("Speaker", back_populates="event_links")