from sqlalchemy.ext.asyncio import create_async_engine
from ..config import settings

engine =  create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Включите для отладки
    pool_pre_ping=True,  # Проверка соединения перед использованием
)