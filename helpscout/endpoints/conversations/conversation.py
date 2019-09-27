from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint
from helpscout.endpoints.conversations.attachment import Attachment
from helpscout.endpoints.conversations.custom_field import CustomField
from helpscout.endpoints.conversations.tag import Tag
from helpscout.endpoints.conversations.thread import Thread


class Conversation(Endpoint):
    def list_conversation(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def get_conversation(self, conversation_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def update_conversation(self, conversation_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            params={**kwargs}
        )

        return response.status_code

    def delete_conversation(self, conversation_id: int) -> int:
        response = requests.delete(
            f'{self.base_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return response.status_code

    def create_conversation(self, **kwargs) -> Dict:
        response = requests.post(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return self._get_json(response)

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
