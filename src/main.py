import asyncio
from queries.orm import create_tables, sync_insert_data, async_insert_data

create_tables()
asyncio.run(async_insert_data())
