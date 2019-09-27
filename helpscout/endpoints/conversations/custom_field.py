import requests

from helpscout.endpoints.endpoint import Endpoint


class CustomField(Endpoint):
    def update_custom_field(self, conversation_id: int, **kwargs) -> int:
        response = requests.put(
            f'{self.base_url}/{conversation_id}/fields',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs},
        )

        return response.status_code
