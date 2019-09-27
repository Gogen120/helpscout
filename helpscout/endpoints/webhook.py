from typing import List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Webhook(Endpoint):
    def list_(self) -> requests.Response:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def get(self, webhook_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def create(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> requests.Response:
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

        return response

    def update(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> requests.Response:
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

        return response

    def delete(self, webhook_id: int) -> requests.Response:
        response = requests.delete(
            f'{self.base_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response
