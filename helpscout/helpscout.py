from typing import Dict, List

import requests


class Base:
    BASE_API_URL = 'https://api.helpscout.net/v2'

    def __init__(self, app_id: str, app_secret: str):
        self._app_id = app_id
        self._app_secret = app_secret
        self._auth_params = self._get_authentication_params()
        self._access_token = self._get_access_token()

    def _get_authentication_params(self) -> Dict:
        response = requests.post(
            f'{self.BASE_API_URL}/oauth2/token',
            data={
                'grant_type': 'client_credentials',
                'client_id': self._app_id,
                'client_secret': self._app_secret
            }
        )

        return response.json()

    def _get_access_token(self) -> str:
        return self._auth_params.get('access_token', '')

    def _get_json(self, response: requests.Response) -> Dict:
        if response.ok:
            return response.json()

        return {}


class Conversations(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._conversation_url = f'{self.BASE_API_URL}/conversations'

    def list_conversation(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self._conversation_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def get_conversation(self, conversation_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self._conversation_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def update_conversation(self, conversation_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self._conversation_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            params={**kwargs}
        )

        return response.status_code

    def delete_conversation(self, conversation_id: int) -> int:
        response = requests.delete(
            f'{self._conversation_url}/{conversation_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return response.status_code

    def create_conversation(self, **kwargs) -> Dict:
        response = requests.post(
            f'{self._conversation_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return self._get_json(response)


class Mailbox(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._mailbox_url = f'{self.BASE_API_URL}/mailboxes'

    def list_mailbox(self) -> Dict:
        response = requests.get(
            f'{self._mailbox_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self._mailbox_url}/{mailbox_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox_fields(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self._mailbox_url}/{mailbox_id}/fields',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def get_mailbox_folders(self, mailbox_id: int) -> Dict:
        response = requests.get(
            f'{self._mailbox_url}/{mailbox_id}/folders',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)


class Tags(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._tag_url = f'{self.BASE_API_URL}/tags'

    def list_tags(self, **kwargs):
        response = requests.get(
            f'{self._tag_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)


class Teams(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._team_url = f'{self.BASE_API_URL}/teams'

    def list_teams(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self._team_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def members(self, team_id: int, **kwargs) -> Dict:
        response = requests.get(
            f'{self._team_url}/{team_id}/members',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)


class Users(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._team_url = f'{self.BASE_API_URL}/users'

    def list_users(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self._team_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def get_user(self, user_id: int) -> Dict:
        response = requests.get(
            f'{self._team_url}/{user_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def get_resource_owner(self) -> Dict:
        response = requests.get(
            f'{self._team_url}/me',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)


class Webhooks(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._webhook_url = f'{self.BASE_API_URL}/webhooks'

    def list_webhook(self):
        response = requests.get(
            f'{self._webhook_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def get_webhook(self, webhook_id: int) -> Dict:
        response = requests.get(
            f'{self._webhook_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return self._get_json(response)

    def create_webhook(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = requests.get(
            f'{self._webhook_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'url': url,
                'events': events,
                'notification': notification,
                'secret': secret,
            }
        )

        return response.status_code

    def update_webhook(
        self, url: str, events: List[str], secret: str, notification: bool = False
    ) -> int:
        response = requests.put(
            f'{self._webhook_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'url': url,
                'events': events,
                'notification': notification,
                'secret': secret,
            }
        )

        return response.status_code

    def delete_webhook(self, webhook_id: int) -> int:
        response = requests.delete(
            f'{self._webhook_url}/{webhook_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            }
        )

        return response.status_code


class Workflows(Base):
    def __init__(self, app_id: str, app_secret: str):
        super().__init__(app_id, app_secret)
        self._workflow_url = f'{self.BASE_API_URL}/workflows'

    def list_workflows(self, **kwargs) -> Dict:
        response = requests.get(
            f'{self._workflow_url}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
            },
            params={**kwargs}
        )

        return self._get_json(response)

    def update_workflow_status(self, workflow_id: int, **kwargs) -> int:
        response = requests.patch(
            f'{self._workflow_url}/{workflow_id}',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={**kwargs}
        )

        return response.status_code

    def run_manual(self, workflow_id: int, conversation_ids: List[int]) -> int:
        response = requests.patch(
            f'{self._workflow_url}/{workflow_id}/run',
            headers={
                'Authorization': f'Bearer {self._access_token}',
                'Content-Type': 'application/json; charset=UTF-8',
            },
            json={
                'conversationIds': conversation_ids,
            }
        )

        return response.status_code
