from bot.converters import chat_message_objects_list_to_list_of_dictionaries
from bot.decorators.transaction import transaction
from bot.entities import ChatMessage
from bot.repositories import ChatRepository
from openai import OpenAI


class ChatGPTCommunicationService:
    def __init__(self, openai_client: OpenAI, chat_repository: ChatRepository) -> None:
        self.openai_client = openai_client
        self.chat_repository = chat_repository

    @transaction
    def get_chatgpt_answer(
        self,
        user_number: str,
        chat_message: ChatMessage,
        model: str = "gpt-3.5-turbo-16k",
    ) -> str:
        self.chat_repository.add_user_message(user_number, chat_message)

        completion_object = self.openai_client.chat.completions.create(
            messages=chat_message_objects_list_to_list_of_dictionaries(
                self.chat_repository.all_user_messages(user_number)
            ),
            model=model,
        )

        completion_content = completion_object.choices[0].message.content

        self.chat_repository.add_user_message(
            user_number, ChatMessage(role="assistant", content=completion_content)
        )

        return completion_content
