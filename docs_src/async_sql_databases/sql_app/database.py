from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@postgresserver/db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
