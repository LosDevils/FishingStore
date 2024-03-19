from typing import List, TYPE_CHECKING
from uuid import uuid4

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType
from sqlalchemy import ForeignKey, UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from inventory.infrastructure.database.models.base import Base

if TYPE_CHECKING:
    from inventory.infrastructure.database.models.characteristic import CharacteristicOrm
    from inventory.infrastructure.database.models.category import CategoryOrm
    from inventory.infrastructure.database.models.subcategory import SubCategoryOrm

storage = FileSystemStorage(path="/tmp")


class ProductOrm(Base):
    __tablename__ = 'products'

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(16))
    price: Mapped[int]
    quantity: Mapped[int]
    description: Mapped[str] = mapped_column(String(255))
    picture: Mapped[ImageType] = mapped_column(ImageType(storage=storage))
    rating: Mapped[float]
    discount: Mapped[int]
    manufacturer: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['CategoryOrm'] = relationship(back_populates='products')

    subcategory_id: Mapped[int] = mapped_column(ForeignKey('subcategories.id'))
    subcategory: Mapped['SubCategoryOrm'] = relationship(back_populates='products')

    characteristics: Mapped[List['CharacteristicOrm']] = relationship(back_populates='product', cascade="all, delete")

    def __repr__(self):
        return self.name
