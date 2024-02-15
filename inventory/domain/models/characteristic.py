from dataclasses import dataclass

from inventory.domain.models.characteristic_type import CharacteristicType


@dataclass
class Characteristic:
    id: int
    value: str
    product_id: int
    characteristic_type_id: int
    characteristic_type: CharacteristicType

