from datetime import datetime
from typing import List

from sqlalchemy import String, text, UUID
from sqlalchemy.orm import Mapped, mapped_column

from inventory.infrastructure.database.models.base import Base


class OrderOrm(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))
    products_id: Mapped[List[UUID]]
    user_id: Mapped[int]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
