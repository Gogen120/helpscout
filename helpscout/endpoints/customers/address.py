from typing import List, Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Address(Endpoint):
    def get(self, customer_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def create(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> int:
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

        return self.process_result_with_status_code(response, 201)

    def update(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> int:
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

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/address',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_result_with_status_code(response, 204)
