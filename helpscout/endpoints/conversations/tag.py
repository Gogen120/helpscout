from typing import List

from helpscout.endpoints.endpoint import Endpoint


class Tag(Endpoint):
    def update(self, conversation_id: int, tags: List[str]) -> int:
        response = self.base_put_request(
            f"{self.base_url}/{conversation_id}/tags", tags=tags
        )

        return self.process_result_with_status_code(response, 204)
