from typing import List

from bot.repositories import ChatRepository
from bot.uow import UnitOfWork


class ChatHistoryManager:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    def delete_user_chat_history(self, user_id: str) -> None:
        with self.uow(repository=ChatRepository) as uow:
            uow.repository.delete_where(user_id=user_id)

            uow.commit()

    def delete_users_chat_history(self, user_ids: List[str]) -> None:
        with self.uow(repository=ChatRepository) as uow:
            for user_id in user_ids:
                uow.repository.delete_where(user_id)

            uow.commit()

    def delete_all_chat_history(self) -> None:
        with self.uow(repository=ChatRepository) as uow:
            uow.repository.delete_all()

            uow.commit()
