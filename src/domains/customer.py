from src.domains.base import DomainBase
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
    
class CustomerRegistration(BaseModel):
    name: str
    email: str
    Address: Address