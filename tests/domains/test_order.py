from src.domains.customer import Address, Customer
from src.domains.product import Product
from src.domains.order import Order, OrderItem, OrderStatus, OrderStatusName

def test_should_creaete_order():
    address: Address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
    customer: Customer = Customer(name="John Doe", email="email@example.com", address=address)

    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED

    product1: Product = Product(
        name="PS5", 
        description="Console ps5 slim", 
        price=499
    )
    assert product1.name == "PS5"
    assert product1.description == "Console ps5 slim"
    assert product1.price == 499.0

    product2: Product = Product(
        name="Xbox Series X", 
        description="Console Xbox Series X", 
        price=399)
    
    assert product2.name == "Xbox Series X"
    assert product2.description == "Console Xbox Series X"
    assert product2.price == 399.0

    item1: OrderItem = OrderItem(
        product_id=product1.id,
        price=product1.price,
        quantity=1
    )

    item2: OrderItem = OrderItem(
        product_id=product2.id,
        price=product2.price,
        quantity=2
    )
  
    order: Order = Order(customer=customer)
    order.set_status(status)
    order.add_item(item1)
    order.add_item(item2)

    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.items) == 2

    status2 = OrderStatus(name=OrderStatusName.PENDING)
    order.set_status(status2)
    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.PENDING

    status3 = OrderStatus(name=OrderStatusName.COMPLETED)
    order.set_status(status3)
    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.COMPLETED

    status4 = OrderStatus(name=OrderStatusName.CANCELED)
    order.set_status(status4)
    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.CANCELED

    total: float = order.total()
    assert total == 499.0 + (399.0 * 2)

     