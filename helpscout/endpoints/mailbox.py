from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Mailbox(Endpoint):
    def list_(self) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def mailbox(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def mailbox_fields(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}/fields',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)

    def mailbox_folders(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self.base_url}/{mailbox_id}/folders',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            }
        )

        return self.process_get_result(response)
