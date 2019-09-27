import requests

from helpscout.endpoints.endpoint import Endpoint


class Productivity(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity',
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

    def first_response_time(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity/first-response-time',
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

    def replies_sent(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity/replies-sent',
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

    def resolution_time(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity/resolution-time',
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

    def resolved(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity/resolved',
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

    def response_time(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/productivity/response-time',
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