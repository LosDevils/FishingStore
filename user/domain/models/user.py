from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    uuid: UUID
    username: str
    balance: int
    email: str
    phone_number: str
    hashed_password: str
