from typing import List

from openai import OpenAI

from bot.entities import ChatMessage
from bot.repositories import ChatRepository
from bot.uow import UnitOfWork


class ChatGPTCommunicationService:
    def __init__(self, openai_client: OpenAI, uow: UnitOfWork) -> None:
        self.uow = uow
        self.openai_client = openai_client

    def get_chatgpt_answer(
        self,
        chat_message: ChatMessage,
        model: str = "gpt-3.5-turbo-16k",
    ) -> str:
        with self.uow(repository=ChatRepository) as uow:
            uow.repository.add(chat_message)
            uow.commit()

            messages = [
                {"role": message.role, "content": message.content}
                for message in self.chat_repository.filter(user_id=chat_message.user_id)
            ]
            completion_content = self.generate_completion_content(
                messages, chat_message, model
            )
            uow.repository.add(
                ChatMessage(
                    role="assistant",
                    content=completion_content,
                    user_id=chat_message.user_id,
                )
            )

            uow.commit()

        return completion_content

    def generate_completion_content(
        self,
        messages: List[ChatMessage],
        chat_message: ChatMessage,
        model: str,
    ) -> str:
        completion_object = self.openai_client.chat.completions.create(
            messages=messages,
            model=model,
        )
        return completion_object.choices[0].message.content
