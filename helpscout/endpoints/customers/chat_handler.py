import requests

from helpscout.endpoints.endpoint import Endpoint


class ChatHandler(Endpoint):
    def get(self, customer_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{customer_id}/chats',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def create(self, customer_id: int, type_: str, value: str) -> requests.Response:
        response = requests.post(
            f'{self.base_url}/{customer_id}/chats',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'type': type_,
                'value': value,
            }
        )

        return response

    def update(self, customer_id: int, chat_id: int, type_: str, value: str) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{customer_id}/chats/{chat_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'type': type_,
                'value': value,
            }
        )

        return response

    def delete(self, customer_id: int, chat_id: int) -> requests.Response:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/chats/{chat_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response
