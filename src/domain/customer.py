from src.domain.base import DomainBase
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Customer(DomainBase):
    name: str
    email: str
    address: Address
    