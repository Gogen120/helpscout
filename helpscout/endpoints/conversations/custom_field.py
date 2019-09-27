from typing import List, Dict, Union

import requests

from helpscout.endpoints.endpoint import Endpoint


class CustomField(Endpoint):
    def update(self, conversation_id: int, fields: List[Dict[str, Union[str, int]]]) -> requests.Response:
        response = requests.put(
            f'{self.base_url}/{conversation_id}/fields',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'fields': fields,
            }
        )

        return response
