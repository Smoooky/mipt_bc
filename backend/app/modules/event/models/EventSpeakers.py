"""
Docstring for backend.app.modules.event.models.Event
Тут описывается модель для СВЯЗИ МЕРОПРИЯТИЯ И СПИКЕРА
"""
from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, TEXT, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone

class eventSpeakers(Base):
    __tablename__ = 'EventSpeakers'

    eventId = Column(Integer, ForeignKey('events.id'), primary_key=True)
    speakerId = Column(Integer, ForeignKey('speakers.id'), primary_key=True)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updatedAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    event = relationship('Event', back_populates='speakerLinks')
    speaker = relationship("Speaker", back_populates="eventLinks")