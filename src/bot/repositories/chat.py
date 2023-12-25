from sqlalchemy import exists
from sqlalchemy.orm import Session

from bot.converters import (
    message_model_to_message_entity,
    message_entity_to_message_model,
)
from bot.entities.chat_message import ChatMessage
from bot.models.message import MessageOrmModel


class ChatRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self) -> list[ChatMessage]:
        messages = self.session.query(MessageOrmModel).all()

        converted = map(message_model_to_message_entity, messages)

        return list(converted)

    def filter(self, user_id: str) -> list[ChatMessage]:
        messages = (
            self.session.query(MessageOrmModel)
            .where(MessageOrmModel.user_id == user_id)
            .all()
        )

        converted = map(message_model_to_message_entity, messages)

        return list(converted)

    def add(self, message: ChatMessage) -> None:
        message_orm_model = message_entity_to_message_model(message)

        self.session.add(message_orm_model)

    def exists(self, user_id: str) -> bool:
        return self.session.scalar(
            exists().where(MessageOrmModel.user_id == user_id).select()
        )

    def delete_where(self, user_id: str) -> None:
        if self.exists(user_id):
            self.session.query(MessageOrmModel).delete()

    def delete_all(self) -> None:
        self.session.query(MessageOrmModel).delete()
