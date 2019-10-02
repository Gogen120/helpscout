from typing import List, Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Workflow(Endpoint):
    def list_(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self.process_get_result(response)

    def update_status(
        self, workflow_id: int, op: str, value: str, path: str
    ) -> int:
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

        return self.process_result_with_status_code(response, 204)

    def run_manual(self, workflow_id: int, conversation_ids: List[int]) -> int:
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

        return self.process_result_with_status_code(response, 204)
