from sqlalchemy.ext.asyncio import create_async_engine
from config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
)