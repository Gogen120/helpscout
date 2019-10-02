from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class User(Endpoint):
    def overall_report(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def conversation_history(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/conversation-history',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def customers_helped(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/customers-helped',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def drilldown(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/drilldown',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def happiness(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/happiness',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def happiness_drilldown(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/ratings',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def replies(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/replies',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def resolution(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/user/resolutions',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'user': user,
                'start': start,
                'end': end,
                **kwargs,
            }
        )

        return self.process_get_result(response)
