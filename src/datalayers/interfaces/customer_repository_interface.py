from src.datalayers.base import RepositoryInterface
from src.domains.customer import Customer, CustomerRegistration

class CustomerRepositoryInterface(RepositoryInterface):
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        raise NotImplementedError

    async def email_already_exists(self, email: str) -> bool:
        raise NotImplementedError