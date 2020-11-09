from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DB_URL = "postgresql+asyncpg://user:password@postgresserver/db"

engine = create_async_engine(POSTGRES_DB_URL)

Base = declarative_base()
