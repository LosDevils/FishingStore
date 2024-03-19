from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from inventory.infrastructure.database.models.base import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("subcategory_id", ForeignKey("subcategories.id"), primary_key=True),
    Column("characteristic_type_id", ForeignKey("characteristic_types.id"), primary_key=True),
)
