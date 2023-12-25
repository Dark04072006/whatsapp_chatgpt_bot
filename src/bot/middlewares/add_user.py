from typing import Any

from bot.core.container import uow as unit_of_work
from bot.entities.user import User
from bot.repositories import UserRepository


def add_user_middleware(event: dict[str, Any]) -> None:
    sender_data = event["senderData"]
    user_id = sender_data["sender"]
    username = sender_data["senderName"]

    with unit_of_work(UserRepository) as uow:
        if not uow.repository.exists(user_id):
            uow.repository.add(
                User(role="user", username=username, whatsapp_id=user_id)
            )
            uow.commit()
