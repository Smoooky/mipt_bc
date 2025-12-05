"""
Docstring for backend.app.modules.auth.models.User
Тут будет описываться модель ПОЛЬЗОВАТЕЛЯ
"""
from core.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
import enum
from datetime import datetime, timezone

class UserRole(enum.Enum):
    MEMBER = 'member'
    ORGANIZER = 'organizer'
    MANAGER = 'manager'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    fullName = Column(String, unique=True, nullable=False)
    techRole = Column(Enum(UserRole), default=UserRole.MEMBER)
    clubRole = Column(String, default='Участник')
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)