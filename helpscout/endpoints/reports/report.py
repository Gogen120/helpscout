from typing import Dict

from helpscout.endpoints.endpoint import Endpoint
from helpscout.endpoints.reports.company import Company
from helpscout.endpoints.reports.conversation import Conversation
from helpscout.endpoints.reports.doc import Doc
from helpscout.endpoints.reports.happiness import Happiness
from helpscout.endpoints.reports.productivity import Productivity
from helpscout.endpoints.reports.user import User


class Report(Endpoint):
    def chat_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/chat',
            start=start, end=end, **kwargs
        )

        return response

    def email_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/email',
            start=start, end=end, **kwargs
        )

        return response

    def phone_report(self, start: str, end: str, **kwargs) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/phone',
            start=start, end=end, **kwargs
        )

        return response

    @property
    def company(self) -> Company:
        return Company(client=self.client, base_url=self.base_url)

    @property
    def conversation(self) -> Conversation:
        return Conversation(client=self.client, base_url=self.base_url)

    @property
    def doc(self) -> Doc:
        return Doc(client=self.client, base_url=self.base_url)

    @property
    def happiness(self) -> Happiness:
        return Happiness(client=self.client, base_url=self.base_url)

    @property
    def productivity(self) -> Productivity:
        return Productivity(client=self.client, base_url=self.base_url)

    @property
    def user(self) -> User:
        return User(client=self.client, base_url=self.base_url)
