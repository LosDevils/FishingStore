from dataclasses import dataclass
from typing import List

from inventory.domain.models.characteristic import Characteristic


# from inventory.domain.models.subcategory import SubCategory

@dataclass
class CharacteristicType:
    id: int
    characteristic_name: str
    # subcategory_id: int
    # subcategory: SubCategory
    characteristic_instance: List[Characteristic]
