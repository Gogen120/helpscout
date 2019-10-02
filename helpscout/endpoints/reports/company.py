from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Company(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
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

        return self.process_get_result(response)

    def customers_helped(self, start: str, end: str, **kwargs) -> Dict:
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

        return self.process_get_result(response)

    def drilldown(self, start: str, end: str, range_: str, **kwargs) -> Dict:
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

        return self.process_get_result(response)
