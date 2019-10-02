from typing import List, Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Webhook(Endpoint):
    def list_(self) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def get(self, webhook_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def create(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'url': url,
                'events': events,
                'notification': notification,
                'secret': secret,
            }
        )

        return self.process_result_with_status_code(response, 201)

    def update(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = requests.put(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'url': url,
                'events': events,
                'notification': notification,
                'secret': secret,
            }
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, webhook_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_result_with_status_code(response, 204)
