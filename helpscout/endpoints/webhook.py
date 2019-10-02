from typing import List, Dict

from helpscout.endpoints.endpoint import Endpoint


class Webhook(Endpoint):
    def list_(self) -> Dict:
        response = self.base_get_request(self.base_url)

        return self.process_get_result(response)

    def get(self, webhook_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{webhook_id}',
        )

        return self.process_get_result(response)

    def create(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = self.base_post_request(
            f'{self.base_url}', url=url, events=events,
            notification=notification, secret=secret,
        )

        return self.process_result_with_status_code(response, 201)

    def update(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = self.base_put_request(
            f'{self.base_url}', url=url, events=events,
            notification=notification, secret=secret,
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, webhook_id: int) -> int:
        response = self.base_delete_request(f'{self.base_url}/{webhook_id}')

        return self.process_result_with_status_code(response, 204)
