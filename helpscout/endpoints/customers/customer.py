from typing import Dict

from helpscout.endpoints.customers.address import Address
from helpscout.endpoints.customers.chat_handler import ChatHandler
from helpscout.endpoints.customers.email import Email
from helpscout.endpoints.customers.phone import Phone
from helpscout.endpoints.customers.social_profile import SocialProfile
from helpscout.endpoints.customers.website import Website
from helpscout.endpoints.endpoint import Endpoint


class Customer(Endpoint):
    def list(self, **kwargs) -> Dict:
        response = self.base_get_request(self.base_url, **kwargs)

        return self.process_get_result(response)

    def get(self, customer_id: int, **kwargs) -> Dict:
        response = self.base_get_request(f"{self.base_url}/{customer_id}", **kwargs)

        return self.process_get_result(response)

    def create(self, first_name: str, **kwargs) -> int:
        response = self.base_post_request(self.base_url, firstName=first_name, **kwargs)

        return self.process_result_with_status_code(response, 201)

    def update(self, customer_id: int, first_name: str, **kwargs) -> int:
        response = self.base_put_request(
            f"{self.base_url}/{customer_id}", firstName=first_name, **kwargs
        )

        return self.process_result_with_status_code(response, 204)

    @property
    def address(self) -> Address:
        return Address(client=self.client, base_url=self.base_url)

    @property
    def chat_handler(self) -> ChatHandler:
        return ChatHandler(client=self.client, base_url=self.base_url)

    @property
    def email(self) -> Email:
        return Email(client=self.client, base_url=self.base_url)

    @property
    def phone(self) -> Phone:
        return Phone(client=self.client, base_url=self.base_url)

    @property
    def social_profile(self) -> SocialProfile:
        return SocialProfile(client=self.client, base_url=self.base_url)

    @property
    def website(self) -> Website:
        return Website(client=self.client, base_url=self.base_url)
