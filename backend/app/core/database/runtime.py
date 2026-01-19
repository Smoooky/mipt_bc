from app.core.config import settings
from .engine import create_db_engine

engine = create_db_engine(settings.DATABASE_URL)