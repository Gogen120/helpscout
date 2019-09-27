import requests

from helpscout.endpoints.endpoint import Endpoint


class Doc(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/docs',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return response
