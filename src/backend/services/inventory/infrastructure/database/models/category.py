from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from inventory.infrastructure.database.models.base import Base
from inventory.infrastructure.database.models.product import ProductOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm


class CategoryOrm(Base):
    __tablename__ = 'product_categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))
    products: Mapped[List['ProductOrm']] = relationship(back_populates='category')
    subcategories: Mapped[List['SubCategoryOrm']] = relationship(back_populates='category')
