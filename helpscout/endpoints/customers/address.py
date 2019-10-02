from typing import List, Dict

from helpscout.endpoints.endpoint import Endpoint


class Address(Endpoint):
    def get(self, customer_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{customer_id}/address',
        )

        return response

    def create(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{customer_id}/address',
            city=city, state=state, postal_code=postal_code,
            country=country, lines=lines,
        )

        return self.process_result_with_status_code(response, 201)

    def update(
        self, customer_id: int, city: str, state: str,
        postal_code: str, country: str, lines: List[str]
    ) -> int:
        response = self.base_put_request(
            f'{self.base_url}/{customer_id}/address',
            city=city, state=state, postal_code=postal_code,
            country=country, lines=lines,
        )

        return self.process_result_with_status_code(response, 204)

    def delete(self, customer_id: int) -> int:
        response = self.base_delete_request(
            f'{self.base_url}/{customer_id}/address',
        )

        return self.process_result_with_status_code(response, 204)
