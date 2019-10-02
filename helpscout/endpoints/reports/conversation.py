from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Conversation(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations',
            start=start, end=end, **kwargs
        )

        return response

    def volumes_by_channel(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/volume-by-channel',
            start=start, end=end, **kwargs
        )

        return response

    def busiest_time_of_day(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/busy-times',
            start=start, end=end, **kwargs
        )

        return response

    def drilldown(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/drilldown',
            start=start, end=end, **kwargs
        )

        return response

    def drilldown_by_field(
        self, start: str, end: str, field: str, fieldid: int, **kwargs
    ) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/fields-drilldown',
            start=start, end=end, field=field, fieldid=fieldid,
            **kwargs
        )

        return response

    def new(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/new',
            start=start, end=end, **kwargs
        )

        return response

    def new_drilldown(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/new-drilldown',
            start=start, end=end, **kwargs
        )

        return response

    def received_messages(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/conversations/received-messages',
            start=start, end=end, **kwargs
        )

        return response
