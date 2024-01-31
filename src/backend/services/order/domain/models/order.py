from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID


@dataclass
class Order:
    id: int
    products_id: List[UUID]
    user_id: int
    status: str
    created_at: datetime
