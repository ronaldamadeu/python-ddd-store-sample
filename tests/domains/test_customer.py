from src.domains.customer import Address, Customer

def test_should_creaete_customer():
    address: Address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
    customer: Customer = Customer(name="John Doe", email="email@example.com", address=address)
    
    assert customer.name == "John Doe"
    assert customer.email == "email@example.com"

    assert customer.address.street == "123 Main St"
    assert customer.address.city == "Anytown"
    assert customer.address.state == "CA"
    assert customer.address.zip_code == "12345"
    assert customer.address.street == "123 Main St"
