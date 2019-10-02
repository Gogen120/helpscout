from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Website(Endpoint):
    def list_(self, customer_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{customer_id}/websites',
        )

        return response

    def create(self, customer_id: int, value: str) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{customer_id}/websites',
            value=value,
        )

        return self.process_result_with_status_code(response, 201)

    def update(self, customer_id: int, website_id: int, value: str) -> int:
        response = self.base_put_request(
            f'{self.base_url}/{customer_id}/websites/{website_id}',
            value=value,
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int, website_id: int) -> int:
        response = self.base_delete_request(
            f'{self.base_url}/{customer_id}/websites/{website_id}',
        )

        return self.process_result_with_status_code(response, 204)
