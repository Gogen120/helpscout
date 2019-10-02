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

    def base_get_request(self, base_url, **kwargs) -> requests.Response:
        response = requests.get(
            base_url,
            headers={
                'Authorization': f'Bearer {self.client.access_token}'
            },
            params={**kwargs}
        )

        return response

    def base_put_request(self, base_url, **kwargs) -> requests.Response:
        response = requests.put(
            base_url,
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response

    def base_patch_request(self, base_url, **kwargs) -> requests.Response:
        response = requests.patch(
            base_url,
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response

    def base_post_request(self, base_url, **kwargs) -> requests.Response:
        response = requests.post(
            base_url,
            headers={
                'Authorization': f'Bearer {self.client.access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response

    def base_delete_request(self, base_url, **kwargs) -> requests.Response:
        response = requests.delete(
            base_url,
            headers={
                'Authorization': f'Bearer {self.client.access_token}'
            }
        )

        return response
