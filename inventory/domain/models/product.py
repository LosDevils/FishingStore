from dataclasses import dataclass
from typing import List
from uuid import UUID

from inventory.domain.models.category import Category
from inventory.domain.models.characteristic import Characteristic
from inventory.domain.models.subcategory import SubCategory


@dataclass
class Product:
    uuid: UUID
    name: str
    price: int
    quantity: int
    description: str
    picture: bytes
    rating: float
    discount: int
    manufacturer: str
    category_id: int
    category: Category
    subcategory_id: int
    subcategory: SubCategory
    characteristics: List[Characteristic]

