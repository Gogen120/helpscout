import requests

from helpscout.endpoints.endpoint import Endpoint


class Happiness(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/happiness',
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

    def ratings(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/happiness/ratings',
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
