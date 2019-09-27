import requests

from helpscout.endpoints.endpoint import Endpoint
from helpscout.endpoints.customers.address import Address
from helpscout.endpoints.customers.chat_handler import ChatHandler
from helpscout.endpoints.customers.email import Email
from helpscout.endpoints.customers.phone import Phone
from helpscout.endpoints.customers.social_profile import SocialProfile
from helpscout.endpoints.customers.website import Website


class Customer(Endpoint):
    def list_(self, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response

    def get(self, customer_id: int, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{customer_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response

    def create(self, first_name: str, **kwargs) -> requests.Response:
        response = requests.post(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'firstName': first_name,
                **kwargs,
            }
        )

        return response

    def update(self, customer_id: int, first_name: str, **kwargs) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{customer_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'firstName': first_name,
                **kwargs,
            }
        )

        return response

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
