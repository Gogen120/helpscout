from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Happiness(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/happiness", start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def ratings(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/happiness/ratings", start=start, end=end, **kwargs
        )

        return self.process_get_result(response)
