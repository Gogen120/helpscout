from typing import Dict

import requests


class Endpoint:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url

    def _get_json(self, response: requests.Response) -> Dict:
        if response.ok:
            return response.json()

        return {}
