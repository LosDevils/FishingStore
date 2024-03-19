from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.base import Base

if TYPE_CHECKING:
    from inventory.infrastructure.database.models.product import ProductOrm
    from inventory.infrastructure.database.models.characteristic_type import CharacteristicTypeOrm


class CharacteristicOrm(Base):
    __tablename__ = 'characteristics'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str] = mapped_column(String(16))

    product_id: Mapped[UUID] = mapped_column(ForeignKey('products.uuid'))
    product: Mapped["ProductOrm"] = relationship(back_populates='characteristics')

    characteristic_type_id: Mapped[int] = mapped_column(ForeignKey('characteristic_types.id'))
    characteristic_type: Mapped['CharacteristicTypeOrm'] = relationship(lazy='joined')

    def __repr__(self):
        return f"{self.characteristic_type.characteristic_name} - {self.value}"
