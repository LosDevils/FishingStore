from dataclasses import dataclass
from typing import List

from inventory.domain.models.category import Category
from inventory.domain.models.characteristic_type import CharacteristicType
from inventory.domain.models.product import Product


@dataclass
class SubCategory:
    id: int
    name: str
    characteristic_type_id: int
    characteristic_types: List[CharacteristicType]
    category_id: int
    category: Category
    products: List[Product]
