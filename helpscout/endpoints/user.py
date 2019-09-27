import requests

from helpscout.endpoints.endpoint import Endpoint


class User(Endpoint):
    def list_(self, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response

    def user(self, user_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{user_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def resource_owner(self) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/me',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response
