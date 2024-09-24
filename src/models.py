from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class WorkersORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
