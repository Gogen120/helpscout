from typing import Dict

import requests

from helpscout.endpoints.conversations.conversation import Conversation
from helpscout.endpoints.customers.customer import Customer
from helpscout.endpoints.mailbox import Mailbox
from helpscout.endpoints.reports.report import Report
from helpscout.endpoints.tag import Tag
from helpscout.endpoints.team import Team
from helpscout.endpoints.user import User
from helpscout.endpoints.webhook import Webhook
from helpscout.endpoints.workflow import Workflow


class Client:
    BASE_API_URL = "https://api.helpscout.net/v2"

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
            f"{self.BASE_API_URL}/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": self._app_id,
                "client_secret": self._app_secret,
            },
        )

        return response.json()

    @property
    def auth_params(self):
        return self._auth_params

    def update_access_token(self):
        self._auth_params = self._get_authentication_params()

    def _get_access_token(self) -> str:
        return self._auth_params.get("access_token", "")

    @property
    def conversation(self) -> Conversation:
        return Conversation(client=self, base_url=f"{self.BASE_API_URL}/conversations")

    @property
    def customer(self) -> Customer:
        return Customer(client=self, base_url=f"{self.BASE_API_URL}/customers")

    @property
    def mailbox(self) -> Mailbox:
        return Mailbox(client=self, base_url=f"{self.BASE_API_URL}/mailboxes")

    @property
    def report(self) -> Report:
        return Report(client=self, base_url=f"{self.BASE_API_URL}/reports")

    @property
    def tag(self) -> Tag:
        return Tag(client=self, base_url=f"{self.BASE_API_URL}/tags")

    @property
    def team(self) -> Team:
        return Team(client=self, base_url=f"{self.BASE_API_URL}/teams")

    @property
    def user(self) -> User:
        return User(client=self, base_url=f"{self.BASE_API_URL}/users")

    @property
    def webhook(self) -> Webhook:
        return Webhook(client=self, base_url=f"{self.BASE_API_URL}/webhooks")

    @property
    def workflow(self) -> Workflow:
        return Workflow(client=self, base_url=f"{self.BASE_API_URL}/workflows")
