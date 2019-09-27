from typing import List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Workflow(Endpoint):
    def list_(self, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response

    def update_status(
        self, workflow_id: int, op: str, value: str, path: str
    ) -> requests.Response:
        response = requests.patch(
            f'{self.base_url}/{workflow_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'op': op,
                'value': value,
                'path': path,
            }
        )

        return response

    def run_manual(self, workflow_id: int, conversation_ids: List[int]) -> requests.Response:
        response = requests.patch(
            f'{self.base_url}/{workflow_id}/run',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'conversationIds': conversation_ids,
            }
        )

        return response
