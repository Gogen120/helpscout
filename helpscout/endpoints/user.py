from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class User(Endpoint):
    def list_users(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def get_user(self, user_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{user_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def get_resource_owner(self) -> Dict:
        response = requests.get(
            f'{self.base_url}/me',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)
