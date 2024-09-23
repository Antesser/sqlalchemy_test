import asyncio
from typing import AsyncGenerator

from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from config import settings

sync_engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)


async_engine = create_async_engine(settings.DATABASE_URL_psycopg)


# metadata = MetaData()

# DATABASE_URL = (
#     f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# class Base(DeclarativeBase):
#     pass


# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
