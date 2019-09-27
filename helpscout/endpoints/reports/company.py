import requests

from helpscout.endpoints.endpoint import Endpoint


class Company(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/company',
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

    def customers_helped(self, start: str, end: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/company/customers-helped',
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

    def drilldown(self, start: str, end: str, range_: str, **kwargs) -> requests.Response:
        response = requests.get(
            f'{self.base_url}/company/drilldown',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'start': start,
                'end': end,
                'range': range_,
                **kwargs,
            }
        )

        return response
