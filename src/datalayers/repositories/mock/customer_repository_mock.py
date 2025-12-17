from src.datalayers.interfaces.customer_repository_interface import CustomerRepositoryInterface
from src.datalayers.repositories.mock.memdb import CUSTOMER_DB
from src.domains.customer import Customer, Address

class CustomerRepositoryMock(CustomerRepositoryInterface):
    async def register(self, customer_registration):
        address = Address(street="", city="", state="", zip_code="")
        new_customer = Customer(
            name=customer_registration.name,
            email=customer_registration.email,
            address=address
        )
        CUSTOMER_DB.append(new_customer)
        return new_customer

    async def email_already_exists(self, email: str) -> bool:
        email_exists = filter(lambda customer: customer.email == email, CUSTOMER_DB)
        return len(list(email_exists)) > 0
        #return any(customer.email == email for customer in CUSTOMER_DB)