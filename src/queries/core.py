from sqlalchemy import insert, text
from models import metadata, table_workers

from database import async_engine, sync_engine


async def get_async_engine():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")


def get_sync_engine():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")
