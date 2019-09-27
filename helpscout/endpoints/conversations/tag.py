from typing import List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Tag(Endpoint):
    def update(self, conversation_id: int, tags: List[str]) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{conversation_id}/tags',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'tags': tags,
            }
        )

        return response