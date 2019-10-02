from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Conversation(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations',
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

    def volumes_by_channel(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/volume-by-channel',
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

    def busiest_time_of_day(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/busy-times',
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

    def drilldown(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/drilldown',
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

    def drilldown_by_field(
        self, start: str, end: str, field: str, fieldid: int, **kwargs
    ) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/fields-drilldown',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={
                'start': start,
                'end': end,
                'field': field,
                'fieldid': fieldid,
                **kwargs,
            }
        )

        return self.process_get_result(response)

    def new(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/new',
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

    def new_drilldown(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/new-drilldown',
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

    def received_messages(self, start: str, end: str, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}/conversations/received-messages',
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
