from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import Engine

def create_db_engine(database_url: str) -> Engine:
    return create_async_engine(database_url)