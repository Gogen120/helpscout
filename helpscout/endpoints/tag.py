from typing import Dict

import requests

from helpscout.endpoints.endpoint import Endpoint


class Tag(Endpoint):
    def list_tags(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self.base_url}',
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)
