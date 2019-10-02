from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Tag(Endpoint):
    def list_(self, **kwargs) -> Dict:
        response = self.base_get_request(self.base_url, **kwargs)

        return response
