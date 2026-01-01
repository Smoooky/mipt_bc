"""
Docstring for backend.app.modules.auth.models.User
Тут будет описываться модель ПОЛЬЗОВАТЕЛЯ
"""
from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.dialects.postgresql import ENUM as PGEnum
from sqlalchemy.orm import relationship, declared_attr

import enum
from datetime import datetime, timezone

class UserRole(str, enum.Enum):
    MEMBER = 'member'
    ORGANIZER = 'organizer'
    MANAGER = 'manager'
    ADMIN = 'admin'

user_role_enum = PGEnum(UserRole, name='userrole', create_type=False)

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, unique=False, nullable=False)
    tech_role = Column(user_role_enum, default=UserRole.MEMBER) # Используется для проверки доступа на платформе
    club_role = Column(String, default='Участник') # !!! НЕ используется для проверки доступа. Не влияет на доступ ВООБЩЕ. Только человеческое описание для UI 
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)

    @declared_attr
    def notifications(cls):
        from app.modules.notify.models import EventNotification
        return relationship(
            'EventNotification',
            back_populates='user',
            cascade='all, delete-orphan'
        )

    @declared_attr
    def delivery_jobs(cls):
        from app.modules.notify.models import DeliveryJob
        return relationship(
            'DeliveryJob',
            back_populates='user',
            cascade='all, delete-orphan'
        )
    sent_invites = relationship(
        "Invite",
        back_populates="invited_by",
        foreign_keys="Invite.invited_by_id"
    )

    used_invites = relationship(
        "Invite",
        back_populates="used_by",
        foreign_keys="Invite.used_by_id"
    )