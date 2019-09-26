from typing import Dict, List

import requests

from helpscout.endpoints.endpoint import Endpoint


class Workflow(Endpoint):
    def list_workflows(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def update_workflow_status(self, workflow_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self.base_url}/{workflow_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

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

        return response.status_code
