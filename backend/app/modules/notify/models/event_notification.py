"""
Docstring for backend.app.modules.notify.models.Notification
Здесь описывается модель УВЕДОМЛЕНИЯ. Примечание: Данные уведомления видит пользователь
"""
from app.core.database.base_model import Base
from sqlalchemy import Column, Integer, JSON, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import enum

class NotificationType(enum.Enum):
    # Events
    EVENT_CREATED = 'event.created'
    EVENT_UPDATED = 'event.updated'
    EVENT_START_SOON = 'event.start_soon'
    EVENT_STARTED = 'event.started'
    EVENT_ENDED = 'event.ended'


    # Roles
    ADDED_AS_MANAGER = 'role.added_manager'
    ADDED_AS_ORGANIZER = 'role.added_orginizer'
    ADDED_AS_MEMBER = 'role.added_member'

    REMOVED_AS_MANAGER = 'role.removed_manager'
    REMOVED_AS_ORGANIZER = 'role.removed_orginizer'

    # Commentsdelivered
    NEW_COMMENT = 'comment.new' # Пока не нужно на самом деле, но пусть будет

    # ANALYTICS
    ANALYTICS_REPORT_READY = 'analytics.report_ready'

class EventNotification(Base):
    __tablename__ = 'EventNotifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id', ondelete='CASCADE'))
    type = Column(Enum(NotificationType), nullable=False)
    payload = Column(JSON, nullable=False)
    read_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship('User', back_populates='notifications')