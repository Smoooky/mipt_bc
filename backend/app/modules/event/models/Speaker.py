"""
Docstring for backend.app.modules.event.models.Speaker
Тут описывается модель СПИКЕРА
"""
from ....core.database.base_model import Base
from sqlalchemy import Column, Integer, String, TEXT, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Speaker(Base):
    __tablename__ = 'Speakers'

    id = Column(Integer, primary_key=True)
    fullName = Column(String, nullable=False)
    bio = Column(TEXT, nullable=True)
    position = Column(String, nullable=False) # Position ну типо должность у человека
    company = Column(String, nullable=False)
    photoURL = Column(String, nullable=True)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updatedAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    event_links = relationship("EventSpeaker", back_populates="speaker")
    events = relationship("Event", secondary="EventSpeakers", viewonly=True)