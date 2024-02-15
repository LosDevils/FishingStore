from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.base import Base


class CharacteristicTypeOrm(Base):
    __tablename__ = 'characteristic_types'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    characteristic_name: Mapped[str] = mapped_column(String(16))
    # subcategory_id: Mapped[int] = mapped_column(ForeignKey('product_subcategories.id', ondelete='CASCADE'))
    # subcategory: Mapped['SubCategoryOrm'] = relationship(back_populates='characteristic_types')

# Какая-то хуйня с категорией, нахуй тут обратная связь, обдумай
