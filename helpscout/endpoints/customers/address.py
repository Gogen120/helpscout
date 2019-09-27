from typing import List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Address(Endpoint):
    def get(self, customer_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def create(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> requests.Response:
        response = requests.post(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'city': city,
                'state': state,
                'postal_code': postal_code,
                'country': country,
                'lines': lines,
            }
        )

        return response

    def update(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'city': city,
                'state': state,
                'postal_code': postal_code,
                'country': country,
                'lines': lines,
            }
        )

        return response

    def delete(self, customer_id: int) -> requests.Response:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response
