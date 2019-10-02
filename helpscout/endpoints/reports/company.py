from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Company(Endpoint):
    def overall_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/company',
            start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def customers_helped(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/company/customers-helped',
            start=start, end=end, **kwargs
        )

        return self.process_get_result(response)

    def drilldown(self, start: str, end: str, range_: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/company/drilldown',
            start=start, end=end, range=range_, **kwargs
        )

        return self.process_get_result(response)
