from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Phone(Endpoint):
    def get(self, customer_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{customer_id}/phones',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def create(self, customer_id: int, type_: str, value: str) -> int:
        response = requests.post(
            f'{self.base_url}/{customer_id}/phones',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'type': type_,
                'value': value,
            }
        )

        return response.status_code

    def update(self, customer_id: int, phone_id: int, type_: str, value: str) -> int:
        response = requests.put(
            f'{self.base_url}/{customer_id}/phones/{phone_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'type': type_,
                'value': value,
            }
        )

        return response.status_code

    def delete(self, customer_id: int, phone_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/phones/{phone_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response.status_code
