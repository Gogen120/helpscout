from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Team(Endpoint):
    def list(self, **kwargs) -> Dict:
        response = self.base_get_request(self.base_url, **kwargs)

        return self.process_get_result(response)

    def members(self, team_id: int, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/members', **kwargs,
        )

        return self.process_get_result(response)
