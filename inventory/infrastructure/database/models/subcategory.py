from typing import List, TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.association_table import association_table
from inventory.infrastructure.database.models.base import Base
from inventory.infrastructure.database.models.category import CategoryOrm

if TYPE_CHECKING:
    from inventory.infrastructure.database.models.characteristic_type import CharacteristicTypeOrm
    from inventory.infrastructure.database.models.product import ProductOrm


class SubCategoryOrm(Base):
    __tablename__ = 'subcategories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(16))
    # characteristic_type_id: Mapped[int] = mapped_column(ForeignKey('characteristic_types.id'))
    characteristic_types: Mapped[List['CharacteristicTypeOrm']] = relationship(secondary=association_table,
                                                                               back_populates='subcategories',
                                                                               cascade="all, delete")
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['CategoryOrm'] = relationship(back_populates='subcategories')
    products: Mapped[List['ProductOrm']] = relationship(back_populates='subcategory', cascade="all, delete")

    def __repr__(self):
        return self.name