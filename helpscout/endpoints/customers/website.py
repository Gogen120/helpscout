import requests

from helpscout.endpoints.endpoint import Endpoint


class Website(Endpoint):
    def get(self, customer_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{customer_id}/websites',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def create(self, customer_id: int, value: str) -> requests.Response:
        response = requests.post(
            f'{self.base_url}/{customer_id}/websites',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'value': value,
            }
        )

        return response

    def update(self, customer_id: int, website_id: int, value: str) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{customer_id}/websites/{website_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'value': value,
            }
        )

        return response

    def delete(self, customer_id: int, website_id: int) -> requests.Response:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/websites/{website_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response
