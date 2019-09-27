import requests

from helpscout.endpoints.endpoint import Endpoint


class Team(Endpoint):
    def list_(self, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response

    def members(self, team_id: int, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/{team_id}/members',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return response
