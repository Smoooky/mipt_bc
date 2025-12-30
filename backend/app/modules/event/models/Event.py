"""
Docstring for backend.app.modules.event.models.Event
Тут описывается модель СОБЫТИЯ
"""
from app.core.database.base_model import Base
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

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(TEXT, nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=True)
    status = Column(Enum(EventStatus), default=EventStatus.FUTURE)
    irl_meeting_space = Column(String, nullable=True) # Мероприятие может быть либо в ирл либо в онлайн, поэтому и то и то опционально. Но лучше как-то проверять, что одно из этого точно есть
    online_meeting_space = Column(String, nullable=True)
    stream_link = Column(String, nullable=True)
    cover_url = Column(String, nullable=True) # Если что, я не знаю как мы будем обложку хранить, поэтому тут пока что именно такое тестовое название таблицы
    registration_link = Column(String, nullable=False) # В use-кейсах указан этот параметр
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    speaker_links = relationship('EventSpeaker', back_populates='events')
    speakers = relationship('Speaker', secondary='EventSpeakers', viewonly=True)

# Проверка: хотя бы одно поле локации
@event.listens_for(Event, "before_insert")
@event.listens_for(Event, "before_update")
def check_location(mapper, connection, target):
    if not target.irl_meeting_space and not target.online_meeting_space:
        raise ValueError("Event must have either IRL or online meeting space")