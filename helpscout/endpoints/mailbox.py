from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Mailbox(Endpoint):
    def list_mailbox(self) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox_fields(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}/fields',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox_folders(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}/folders',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self._get_json(response)
