from dataclasses import asdict

from bot.entities.chat_message import ChatMessage
from bot.entities.user import User
from bot.models.message import MessageOrmModel
from bot.models.user import UserOrmModel


def message_model_to_message_entity(message_model: MessageOrmModel) -> ChatMessage:
    return ChatMessage(
        role=message_model.role,
        content=message_model.content,
        user_id=message_model.user_id,
    )


def message_entity_to_message_model(message_entity: ChatMessage) -> MessageOrmModel:
    return MessageOrmModel(**asdict(message_entity))


def user_model_to_user_entity(user_model: UserOrmModel) -> User:
    return User(
        whatsapp_id=user_model.whatsapp_id,
        username=user_model.username,
        role=user_model.role,
    )


def user_entity_to_user_model(user_entity: User) -> UserOrmModel:
    return UserOrmModel(**asdict(user_entity))
