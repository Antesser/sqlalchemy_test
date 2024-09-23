from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    MetaData,
    String,
    Table,
)

metadata = MetaData()

table_workers = Table(
    "workers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
#     Column("figi", String),
#     Column("instrument_type", String, nullable=True),
#     Column(
#         "date", TIMESTAMP(timezone=True), default=datetime.now(timezone.utc)
#     ),
#     Column("type", String),
)
