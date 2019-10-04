from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class User(Endpoint):
    def overall_report(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user", user=user, start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def conversation_history(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/conversation-history",
            user=user,
            start=start,
            end=end,
            **kwargs,
        )

        return self.process_get_result(response)

    def customers_helped(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/customers-helped",
            user=user,
            start=start,
            end=end,
            **kwargs,
        )

        return self.process_get_result(response)

    def drilldown(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/drilldown", user=user, start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def happiness(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/happiness", user=user, start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def happiness_drilldown(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/ratings", user=user, start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def replies(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/replies", user=user, start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def resolution(self, user: int, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/user/resolutions",
            user=user,
            start=start,
            end=end,
            **kwargs,
        )

        return self.process_get_result(response)
