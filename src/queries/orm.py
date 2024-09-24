from sqlalchemy import delete
from models import WorkersORM

from database import (
    Base,
    async_engine,
    sync_engine,
    sync_session_maker,
    async_session_maker,
)


def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def sync_insert_data():
    worker_one = WorkersORM(username="Pax")
    worker_two = WorkersORM(username="Wobiscum")
    with sync_session_maker() as session:
        session.add_all([worker_one, worker_two])
        session.commit()


async def async_insert_data():
    worker_one = WorkersORM(username="Rex")
    worker_two = WorkersORM(username="Shmex")
    async with async_session_maker() as session:
        session.add_all([worker_one, worker_two])
        await session.commit()
