from typing import List, Dict, Union

from helpscout.endpoints.endpoint import Endpoint


class CustomField(Endpoint):
    def update(self, conversation_id: int, fields: List[Dict[str, Union[str, int]]]) -> int:
        response = self.base_put_request(
            f'{self.base_url}/{conversation_id}/fields',
            fields=fields,
        )

        return self.process_result_with_status_code(response, 204)
