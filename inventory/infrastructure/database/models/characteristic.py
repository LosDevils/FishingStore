from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.characteristic_type import CharacteristicTypeOrm
from inventory.infrastructure.database.models.base import Base


class CharacteristicOrm(Base):
    __tablename__ = 'product_characteristics'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[str] = mapped_column(String(16))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.uuid'))
    characteristic_type_id: Mapped[int] = mapped_column(ForeignKey('characteristic_types.id'))
    characteristic_type: Mapped['CharacteristicTypeOrm'] = relationship()
