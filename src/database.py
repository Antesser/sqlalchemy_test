import asyncio
from typing import AsyncGenerator

from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

sync_engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)


async_engine = create_async_engine(settings.DATABASE_URL_asyncpg)


class Base(DeclarativeBase):
    pass


sync_session_maker = sessionmaker(sync_engine, expire_on_commit=False)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
