from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.base import Base
from inventory.infrastructure.database.models.category import CategoryOrm
from inventory.infrastructure.database.models.characteristic_type import CharacteristicTypeOrm
from inventory.infrastructure.database.models.product import ProductOrm


class SubCategoryOrm(Base):
    __tablename__ = 'product_subcategories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))
    characteristic_type_id: Mapped[int] = mapped_column(ForeignKey='characteristic_types.id')
    characteristic_types: Mapped[List['CharacteristicTypeOrm']] = relationship()
    category_id: Mapped[int] = mapped_column(ForeignKey('product_categories.id'))
    category: Mapped['CategoryOrm'] = relationship(back_populates='subcategories')
    products: Mapped[List['ProductOrm']] = relationship(back_populates='subcategory')
