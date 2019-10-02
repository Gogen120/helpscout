from typing import Any, Dict

import requests

from helpscout.endpoints.endpoint import Endpoint
from helpscout.endpoints.conversations.attachment import Attachment
from helpscout.endpoints.conversations.custom_field import CustomField
from helpscout.endpoints.conversations.tag import Tag
from helpscout.endpoints.conversations.thread import Thread


class Conversation(Endpoint):
    def list_(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self.process_get_result(response)

    def get(self, conversation_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self.process_get_result(response)

    def update(self, conversation_id: int, op: str, path: str, value: Any = None) -> int:
        response = requests.patch(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            params={
                'op': op,
                'path': path,
                'value': value,
            }
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, conversation_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_result_with_status_code(response, 204)

    def create(self, **kwargs) -> int:
        response = requests.post(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return self.process_result_with_status_code(response, 201)

    @property
    def attachment(self) -> Attachment:
        return Attachment(client=self.client, base_url=self.base_url)

    @property
    def custom_field(self) -> CustomField:
        return CustomField(client=self.client, base_url=self.base_url)

    @property
    def tag(self) -> Tag:
        return Tag(client=self.client, base_url=self.base_url)

    @property
    def thread(self) -> Thread:
        return Thread(client=self.client, base_url=self.base_url)
