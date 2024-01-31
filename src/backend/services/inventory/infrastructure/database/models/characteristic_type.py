from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.base import Base
from inventory.infrastructure.database.models.characteristic import CharacteristicOrm
from inventory.infrastructure.database.models.subcategory import SubCategoryOrm


class CharacteristicTypeOrm(Base):
    __tablename__ = 'characteristic_types'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    characteristic_name: Mapped[str] = mapped_column(String(16))
    # subcategory_id: Mapped[int] = mapped_column(ForeignKey('product_subcategories.id', ondelete='CASCADE'))
    # subcategory: Mapped['SubCategoryOrm'] = relationship(back_populates='characteristic_types')
    characteristic_instance: Mapped[List['CharacteristicOrm']] = relationship()

# Какая-то хуйня с категорией, нахуй тут обратная связь, обдумай
