from pydantic import BaseModel, Field
from src.domain.base import DomainBase

class OrderStatus(BaseModel):
    name: str 
    
class OrderItem(BaseModel):
    product_id: str
    price: float
    quantity: int

class Order(DomainBase):
    status: list[OrderStatus] = Field(default=[])
    items: list[OrderItem] = Field(default=[])
    total: float