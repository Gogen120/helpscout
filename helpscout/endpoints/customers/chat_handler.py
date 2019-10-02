from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class ChatHandler(Endpoint):
    def list_(self, customer_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{customer_id}/chats',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def create(self, customer_id: int, type_: str, value: str) -> int:
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

        return self.process_result_with_status_code(response, 201)

    def update(self, customer_id: int, chat_id: int, type_: str, value: str) -> int:
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

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int, chat_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{customer_id}/chats/{chat_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_result_with_status_code(response, 204)
