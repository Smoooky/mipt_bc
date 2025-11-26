"""
Docstring for backend.app.core.infrastructure.sqlAlchemy.session
Здесь создается фабрика для создания сессий
"""

from sqlalchemy.orm import sessionmaker
from .engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)