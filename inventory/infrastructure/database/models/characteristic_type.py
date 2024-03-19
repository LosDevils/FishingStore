from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.association_table import association_table
from inventory.infrastructure.database.models.base import Base
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm


class CharacteristicTypeOrm(Base):
    __tablename__ = 'characteristic_types'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    characteristic_name: Mapped[str] = mapped_column(String(16))
    # subcategory_id: Mapped[int] = mapped_column(ForeignKey('subcategories.id', ondelete='CASCADE'))
    subcategories: Mapped[List['SubCategoryOrm']] = relationship(secondary=association_table,
                                                                 back_populates='characteristic_types')

    def __repr__(self):
        return self.characteristic_name
# Какая-то хуйня с категорией, нахуй тут обратная связь, обдумай
