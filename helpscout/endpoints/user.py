from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class User(Endpoint):
    def list(self, **kwargs) -> Dict:
        response = self.base_get_request(self.base_url, **kwargs)

        return self.process_get_result(response)

    def user(self, user_id: int) -> Dict:
        response = self.base_get_request(f"{self.base_url}/{user_id}")

        return self.process_get_result(response)

    def resource_owner(self) -> Dict:
        response = self.base_get_request(f"{self.base_url}/me")

        return self.process_get_result(response)
