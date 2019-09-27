import requests

from helpscout.endpoints.endpoint import Endpoint


class Attachment(Endpoint):
    def get(self, conversation_id: int, attachment_id: int) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}/data',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def delete(self, conversation_id: int, attachment_id: int) -> requests.Response:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}/attachments/{attachment_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response

    def upload(
        self, conversation_id: int, thread_id: int,
        file_name: str, mime_type: str, data: str
    ) -> requests.Response:
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

        return response
