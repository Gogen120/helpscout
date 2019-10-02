from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Attachment(Endpoint):
    def get(self, conversation_id: int, attachment_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}/data',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def delete(self, conversation_id: int, attachment_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_result_with_status_code(response, 204)

    def upload(
        self, conversation_id: int, thread_id: int,
        file_name: str, mime_type: str, data: str
    ) -> int:
        response = requests.post(
            f'{self.base_url}/{conversation_id}/threads{thread_id}/attachments/',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            json={
                'fileName': file_name,
                'mimeType': mime_type,
                'data': data,
            }
        )

        return self.process_result_with_status_code(response, 201)
