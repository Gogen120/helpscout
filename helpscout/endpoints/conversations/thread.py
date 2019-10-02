from typing import Any, Dict

from helpscout.endpoints.endpoint import Endpoint


class Thread(Endpoint):
    def list_(self, conversation_id: int) -> Dict:
        response = self.base_get_request(
            f'{self.base_url}/{conversation_id}/threads',
        )

        return response

    def update(
        self, conversation_id: int, thread_id: int,
        op: str, path: str, value: Any
    ) -> int:
        response = self.base_patch_request(
            f'{self.base_url}/{conversation_id}/threads/{thread_id}',
            op=op, path=path, value=value,
        )

        return self.process_result_with_status_code(response, 204)

    def create_reply_thread(self, conversation_id: int, **kwargs) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{conversation_id}/reply',
            **kwargs,
        )

        return self.process_result_with_status_code(response, 201)

    def create_phone_thread(self, conversation_id: int, **kwargs) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{conversation_id}/phones',
            **kwargs,
        )

        return self.process_result_with_status_code(response, 201)

    def create_note(self, conversation_id: int, **kwargs) -> int:
        response = self.base_post_request(
            f'{self.base_url}/{conversation_id}/notes',
            **kwargs,
        )

        return self.process_result_with_status_code(response, 201)

    def create_customer_thread(self, conversation_id: int, **kwargs) -> int:
        response = response = self.base_post_request(
            f'{self.base_url}/{conversation_id}/customer',
            **kwargs,
        )

        return self.process_result_with_status_code(response, 201)

    def create_chat_thread(self, conversation_id: int, **kwargs) -> int:
        response = response = self.base_post_request(
            f'{self.base_url}/{conversation_id}/chats',
            **kwargs,
        )

        return self.process_result_with_status_code(response, 201)
