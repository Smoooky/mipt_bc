"""
Docstring for backend.app.modules.auth.models.User
Тут будет описываться модель ПОЛЬЗОВАТЕЛЯ
"""
from core.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone

class UserRole(enum.Enum):
    MEMBER = 'member'
    ORGANIZER = 'organizer'
    MANAGER = 'manager'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    fullName = Column(String, unique=True, nullable=False)
    techRole = Column(Enum(UserRole), default=UserRole.MEMBER)
    clubRole = Column(String, default='Участник')
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updatedAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    isActive = Column(Boolean, default=True)

    notifications = relationship(
        'EventNotification',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    delivery_jobs = relationship(
        'DeliveryJob',
        back_populates='user',
        cascade='all, delete-orphan'
    )