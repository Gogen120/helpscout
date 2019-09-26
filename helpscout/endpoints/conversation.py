from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Conversation(Endpoint):
    def list_conversation(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def get_conversation(self, conversation_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def update_conversation(self, conversation_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            params={**kwargs}
        )

        return response.status_code

    def delete_conversation(self, conversation_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response.status_code

    def create_conversation(self, **kwargs) -> Dict:
        response = requests.post(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return self._get_json(response)
