from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Email(Endpoint):
    def list_(self, customer_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{customer_id}/emails',
        )

        return response

    def create(self, customer_id: int, type_: str, value: str) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{customer_id}/emails',
            type=type_, value=value
        )

        return self.process_result_with_status_code(response, 201)

    def update(self, customer_id: int, email_id: int, type_: str, value: str) -> int:
        response = self.base_pus_request(
            f'{self.base_url}/{customer_id}/emails/{email_id}',
            type=type_, value=value
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int, email_id: int) -> int:
        response = self.base_delete_request(
            f'{self.base_url}/{customer_id}/emails/{email_id}',
        )

        return self.process_result_with_status_code(response, 204)
