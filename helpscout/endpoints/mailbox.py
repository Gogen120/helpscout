from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Mailbox(Endpoint):
    def list_(self) -> Dict:
        response = self.base_get_request(self.base_url)

        return response

    def mailbox(self, mailbox_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{mailbox_id}',
        )

        return response

    def mailbox_fields(self, mailbox_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{mailbox_id}/fields',
        )

        return response

    def mailbox_folders(self, mailbox_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{mailbox_id}/folders',
        )

        return response
