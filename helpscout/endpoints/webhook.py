from typing import Dict, List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Webhook(Endpoint):
    def list_webhook(self):
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def get_webhook(self, webhook_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def create_webhook(
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

        return response.status_code

    def update_webhook(
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

        return response.status_code

    def delete_webhook(self, webhook_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response.status_code
