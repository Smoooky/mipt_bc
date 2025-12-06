"""
Docstring for backend.app.modules.notify.models.DeliveryJob
Здесь описывается модель ТЕХНИЧЕСКОГО УВЕДОМЛЕНИЯ. Примечание: Данные уведомления не видит пользователь. Храним мы их, потому что нужно гарантировать их доставку пользователю
"""
from core.database.base_model import Base
from sqlalchemy import Column, Integer, JSON, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import enum

class DeliveryType(enum.Enum):
    # Password
    PASSWORD_RESET = 'password.reset'

    # Email
    VERIFY_EMAIL = 'email.verify'

class DeliveryChannel(enum.Enum):
    EMAIL = 'email'
    TELEGRAM = 'telegram'
    PLATFORM = 'platform'

class DeliveryStatus(enum.Enum):
    PENDING = 'pending'
    DELIVERED = 'delivered'
    FAILED = 'failed'


class DeliveryJob(Base):
    __tablename__ = 'DeliveryJob'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('Users.id', ondelete='CASCADE'))
    channel = Column(Enum(DeliveryChannel), nullable=False)
    payload = Column(JSON, nullable=False)
    status = Column(Enum(DeliveryStatus), default=DeliveryStatus.PENDING)
    attempts = Column(Integer, default=1)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    lastAttemptAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship('User', back_populates='delivery_jobs')