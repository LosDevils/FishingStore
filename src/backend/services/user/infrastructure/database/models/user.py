from uuid import uuid4

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.services.user.infrastructure.database.models.base import Base


class UserOrm(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(16), nullable=False, unique=True)
    balance: Mapped[int] = mapped_column(default=0)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str | None] = mapped_column(default=None, unique=True)
    hashed_password: Mapped[str]
