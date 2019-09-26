from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Team(Endpoint):
    def list_teams(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def members(self, team_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/{team_id}/members',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)
