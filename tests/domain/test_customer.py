from src.domain.customer import Customer

def test_should_creaete_customer():
    customer: Customer = Customer(name="John Doe", email="email@email.com")
    
    assert customer.name == "John Doe"
    assert customer.email == "email@email.com"