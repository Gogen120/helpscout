from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Attachment(Endpoint):
    def get_attachment_data(self, conversation_id: int, attachment_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}/data',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def delete_attachment(self, conversation_id: int, attachment_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response.status_code

    def upload_attachment(self, conversation_id: int, thread_id: int, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/threads{thread_id}/attachments/',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            json={**kwargs}
        )

        return response.status_code
