from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Phone(Endpoint):
    def list(self, customer_id: int) -> Dict:
        response = self.base_get_request(f"{self.base_url}/{customer_id}/phones")

        return self.process_get_result(response)

    def create(self, customer_id: int, type_: str, value: str) -> int:
        response = self.base_post_request(
            f"{self.base_url}/{customer_id}/phones", type=type_, value=value
        )

        return self.process_result_with_status_code(response, 201)

    def update(self, customer_id: int, phone_id: int, type_: str, value: str) -> int:
        response = self.base_post_request(
            f"{self.base_url}/{customer_id}/phones/{phone_id}", type=type_, value=value
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int, phone_id: int) -> int:
        response = self.base_delete_request(
            f"{self.base_url}/{customer_id}/phones/{phone_id}"
        )

        return self.process_result_with_status_code(response, 204)
