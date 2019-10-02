from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Productivity(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity',
            start=start, end=end, **kwargs
        )

        return response

    def first_response_time(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity/first-response-time',
            start=start, end=end, **kwargs
        )

        return response

    def replies_sent(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity/replies-sent',
            start=start, end=end, **kwargs
        )

        return response

    def resolution_time(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity/resolution-time',
            start=start, end=end, **kwargs
        )

        return response

    def resolved(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity/resolved',
            start=start, end=end, **kwargs
        )

        return response

    def response_time(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/productivity/response-time',
            start=start, end=end, **kwargs
        )

        return response
