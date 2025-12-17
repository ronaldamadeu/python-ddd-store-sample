from dataclasses import dataclass
from src.datalayers.interfaces.customer_repository_interface import CustomerRepositoryInterface
from src.services.base import ServiceBase
from src.domains.customer import Customer, CustomerRegistration
from src.services.exceptions.customer_exception import EmailAlreadyExistsException

@dataclass
class CustomerService(ServiceBase):
    repository: CustomerRepositoryInterface

    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        if await self.email_already_exists(customer_registration.email):
            raise EmailAlreadyExistsException()
        
        return await self.repository.register(customer_registration)

    async def email_already_exists(self, email: str) -> bool:
        return await self.repository.email_already_exists(email)