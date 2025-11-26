"""
Docstring for backend.app.core.infrastructure.sqlAlchemy.engine
Здесь создается соединение с бд
"""

from sqlalchemy import create_engine
from .config import config as db_settings

engine = create_engine(
    db_settings.url,
    echo=False,
    future=True
)