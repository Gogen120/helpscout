from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Thread(Endpoint):
    def list_threads(self, conversation_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}/threads',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
        )

        return self._get_json(response)

    def update_thread(self, conversation_id: int, thread_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self.base_url}/{conversation_id}/threads/{thread_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def create_reply_thread(self, conversation_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/reply',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def create_phone_thread(self, conversation_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/phones',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def create_note(self, conversation_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/notes',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def create_customer_thread(self, conversation_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/customer',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def create_chat_thread(self, conversation_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/chats',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code
