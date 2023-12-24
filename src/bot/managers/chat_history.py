from typing import List

from bot.repositories import ChatRepository


class ChatHistoryManager:
    def __init__(self, chat_repository: ChatRepository) -> None:
        self.chat_repository = chat_repository

    def delete_user_chat_history(self, user_number: str) -> None:
        self.chat_repository.delete_user_messages(user_number)

    def delete_users_chat_history(self, user_numbers: List[str]) -> None:
        for user_number in user_numbers:
            self.chat_repository.delete_user_messages(user_number)

    def delete_all_chat_history(self) -> None:
        self.chat_repository.delete_all_messages()
