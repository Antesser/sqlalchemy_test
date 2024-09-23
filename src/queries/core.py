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


def create_tables():
    sync_engine.echo=False
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)
    sync_engine.echo=True


def insert_data():
    with sync_engine.connect() as conn:
        # statement = """insert into table_workers (username) values
        # ('AO First'),
        # ('OOO Second');"""
        statement = insert(table_workers).values([{"username":"Lex"}, {"username":"Luthor"}])
        conn.execute(statement)
        conn.commit()