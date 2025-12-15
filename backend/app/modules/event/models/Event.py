"""
Docstring for backend.app.modules.event.models.Event
Тут описывается модель СОБЫТИЯ
"""
from ....core.database.base_model import Base
from sqlalchemy import Column, Integer, String, TEXT, DateTime, Enum, event
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone

class EventStatus(enum.Enum):
    FUTURE = 'future'
    CURRENT = 'current'
    STARTED = 'started'
    ENDED = 'ended'

class Event(Base):
    __tablename__ = 'Events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(TEXT, nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=True)
    status = Column(Enum(EventStatus), default=EventStatus.FUTURE)
    irlMeetingSpace = Column(String, nullable=True) # Мероприятие может быть либо в ирл либо в онлайн, поэтому и то и то опционально. Но лучше как-то проверять, что одно из этого точно есть
    onlineMeetingSpace = Column(String, nullable=True)
    streamLink = Column(String, nullable=True)
    coverUrl = Column(String, nullable=True) # Если что, я не знаю как мы будем обложку хранить, поэтому тут пока что именно такое тестовое название таблицы
    registrationLink = Column(String, nullable=False) # В use-кейсах указан этот параметр
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updatedAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    speakerLinks = relationship('EventSpeaker', back_populates='event')
    speakers = relationship('Speaker', secondary='EventSpeakers', viewonly=True)

# Проверка: хотя бы одно поле локации
@event.listens_for(Event, "before_insert")
@event.listens_for(Event, "before_update")
def check_location(target):
    if not target.irlMeetingSpace and not target.onlineMeetingSpace:
        raise ValueError("Event must have either IRL or online meeting space")