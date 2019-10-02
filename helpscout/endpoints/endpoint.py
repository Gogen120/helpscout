from typing import Dict

import requests

import helpscout.exceptions as exc


class Endpoint:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    def process_get_result(self, response: requests.Response) -> Dict:
        if response.status_code == 400:
            raise exc.BadRequestException
        elif response.status_code == 401:
            raise exc.NotAuthorizedException
        elif response.status_code == 404:
            return {}

        return response.json()

    def process_result_with_status_code(self, response: requests.Response, status_code):
        if response.status_code != status_code:
            raise exc.BadRequestException

        return response.status_code
