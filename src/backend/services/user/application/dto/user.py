from pydantic import BaseModel, Field, EmailStr
from uuid import UUID


class User(BaseModel):
    uuid: UUID
    username: str = Field(max_length=16, pattern=r'^[a-zA-Z0-9_]+$')
    balance: float = Field(gt=0, decimal_places=2)
    email: EmailStr
    phone_number: str = Field(default=None, max_length=12, pattern=r'^\+\d+$')
    hashed_password: str
