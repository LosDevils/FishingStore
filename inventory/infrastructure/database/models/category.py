from typing import List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from inventory.infrastructure.database.models.base import Base
if TYPE_CHECKING:
    from inventory.infrastructure.database.models.product import ProductOrm
    from inventory.infrastructure.database.models.subcategory import SubCategoryOrm


class CategoryOrm(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))

    products: Mapped[List['ProductOrm']] = relationship(back_populates='category', cascade="all, delete")

    subcategories: Mapped[List['SubCategoryOrm']] = relationship(cascade="all, delete")

    def __repr__(self):
        return self.name
