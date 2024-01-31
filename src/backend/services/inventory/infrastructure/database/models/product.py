from typing import List
from uuid import uuid4

from sqlalchemy import ForeignKey, UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.category import CategoryOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm
from src.backend.services.inventory.infrastructure.database.models.base import Base


class ProductOrm(Base):
    __tablename__ = 'products'

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(16))
    price: Mapped[int]
    quantity: Mapped[int]
    description: Mapped[str] = mapped_column(String(255))
    picture: Mapped[bytes]
    rating: Mapped[float]
    discount: Mapped[int]
    manufacturer: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('product_categories.id'))
    category: Mapped['CategoryOrm'] = relationship(back_populates='products')
    subcategory_id: Mapped[int] = mapped_column(ForeignKey('product_subcategories.id'))
    subcategory: Mapped['SubCategoryOrm'] = relationship(back_populates='')
    characteristics: Mapped[List['CharacteristicOrm']] = relationship()
