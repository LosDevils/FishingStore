from dataclasses import dataclass
from typing import List
from inventory.domain.models.product import Product
from inventory.domain.models.subcategory import SubCategory


@dataclass
class Category:
    id: int
    name: str
    products: List[Product]
    subcategories: List[SubCategory]