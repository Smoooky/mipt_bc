from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from ..models import UserRole
from datetime import datetime, timezone

class Invite(Base):
    __tablename__ = "Invites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, unique=True, nullable=False, index=True)
    role = Column(Enum(UserRole), default=UserRole.MEMBER)

    invited_by_id = Column(Integer, ForeignKey('Users.id', ondelete='SET NULL'), nullable=True)
    used_by_id = Column(Integer, ForeignKey("Users.id", ondelete="SET NULL"), nullable=True)
    
    used_at = Column(DateTime(timezone=True), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    invited_by = relationship(
        'User',
        back_populates='sent_invites',
        foreign_keys=[invited_by_id]
    )

    used_by = relationship(
        'User',
        back_populates='used_invites',
        foreign_keys=[used_by_id]
    )
