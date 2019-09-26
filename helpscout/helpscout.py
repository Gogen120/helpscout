from typing import Dict

import requests

from helpscout.endpoints.conversation import Conversation
from helpscout.endpoints.mailbox import Mailbox
from helpscout.endpoints.tag import Tag
from helpscout.endpoints.team import Team
from helpscout.endpoints.user import User
from helpscout.endpoints.webhook import Webhook
from helpscout.endpoints.workflow import Workflow


class Client:
    BASE_API_URL = 'https://api.helpscout.net/v2'

    def __init__(self, app_id: str, app_secret: str):
        self._app_id = app_id
        self._app_secret = app_secret
        self._auth_params = self._get_authentication_params()
        self._access_token = self._get_access_token()

    @property
    def access_token(self):
        return self._access_token

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

    @property
    def conversation(self):
        return Conversation(client=self, base_url=f'{self.BASE_API_URL}/conversations')

    @property
    def mailbox(self):
        return Mailbox(client=self, base_url=f'{self.BASE_API_URL}/mailboxes')

    @property
    def tag(self):
        return Tag(client=self, base_url=f'{self.BASE_API_URL}/tags')

    @property
    def team(self):
        return Team(client=self, base_url=f'{self.BASE_API_URL}/teams')

    @property
    def user(self):
        return User(client=self, base_url=f'{self.BASE_API_URL}/users')

    @property
    def webhook(self):
        return Webhook(client=self, base_url=f'{self.BASE_API_URL}/webhooks')

    @property
    def workflow(self):
        return Workflow(client=self, base_url=f'{self.BASE_API_URL}/workflows')
