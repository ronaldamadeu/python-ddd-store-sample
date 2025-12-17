from src.services.exceptions.customer_exception import EmailAlreadyExistsException
from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration, Address

import pytest


def test_should_raise_email_already_exists_exception():
    try:
        raise EmailAlreadyExistsException()
    except EmailAlreadyExistsException as e:
        assert str(e) == "Email already exists"

@pytest.mark.asyncio
async def test_should_create_customer_service_with_mock_repository():
    service = CustomerFactory.create_mock()
    assert service is not None
    assert hasattr(service, 'repository')
    assert service.repository.__class__.__name__ == 'CustomerRepositoryMock'

@pytest.mark.asyncio
async def test_should_register_customer_successfully():
    
    service = CustomerFactory.create_mock()
    address: Address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
    customer_registration = CustomerRegistration(name="John Doe", email="email@example.com", Address=address)    
    customer = await service.register(customer_registration)
    assert customer is not None
    assert customer.name == "John Doe"
    assert customer.email == "email@example.com"


@pytest.mark.asyncio
async def test_should_raise_error_duplicated_customer():
    
    service = CustomerFactory.create_mock()
    address: Address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
    customer_duplicated = CustomerRegistration(name="John Doe", email="email@example.com", Address=address)    
    with pytest.raises(EmailAlreadyExistsException):
        await service.register(customer_duplicated)