from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Team(Endpoint):
    def list_(self, **kwargs) -> Dict:
        response = self.base_get_request(self.base_url, **kwargs)

        return response

    def members(self, team_id: int, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/members', **kwargs,
        )

        return response
