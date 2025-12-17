from enum import Enum
from uuid import UUID
from src.domains.customer import Customer
from pydantic import BaseModel, Field
from src.domains.base import DomainBase

class OrderStatusName(str, Enum):
    ACCOMPLISHED = "ACCOMPLISHED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
class OrderStatus(BaseModel):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED) 
    
class OrderItem(BaseModel):
    product_id: UUID
    price: float
    quantity: int

class Order(DomainBase):
    customer: Customer
    status: list[OrderStatus] = Field(default=[])
    items: list[OrderItem] = Field(default=[])

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def set_status(self, status: OrderStatus):
        self.status.append(status)

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)