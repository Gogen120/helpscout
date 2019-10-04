from typing import Dict

from helpscout.endpoints.endpoint import Endpoint


class Attachment(Endpoint):
    def get(self, conversation_id: int, attachment_id: int) -> Dict:
        response = self.base_get_request(
            f"{self.base_url}/{conversation_id}/attachments/{attachment_id}/data"
        )

        return self.process_get_result(response)

    def delete(self, conversation_id: int, attachment_id: int) -> int:
        response = self.base_delete_request(
            f"{self.base_url}/{conversation_id}/attachments/{attachment_id}"
        )

        return self.process_result_with_status_code(response, 204)

    def upload(
        self,
        conversation_id: int,
        thread_id: int,
        file_name: str,
        mime_type: str,
        data: str,
    ) -> int:
        response = self.base_post_request(
            f"{self.base_url}/{conversation_id}/threads{thread_id}/attachments/",
            fileName=file_name,
            mimeType=mime_type,
            data=data,
        )

        return self.process_result_with_status_code(response, 201)
