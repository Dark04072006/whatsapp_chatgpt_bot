from typing import Callable, Any, Literal

from whatsapp_chatbot_python import Notification
from whatsapp_chatbot_python.manager.handler import HandlerType

ChatType = Literal["group", "private"]


def is_group_chat(chat: str) -> bool:
    return chat.endswith("@g.us")


def is_private_chat(chat: str) -> bool:
    return chat.endswith("@c.us")


def check_chat_type(chat_type: ChatType) -> None:
    if chat_type not in ("group", "private"):
        raise ValueError(
            f"Invalid chat type. Must be group or private, not {chat_type}"
        )


def only_for_chat_type(chat_type: ChatType) -> Callable[[HandlerType], HandlerType]:
    """
    Decorator for filtering handlers for a specified chat type, like group or private.

    :param chat_type: The chat type to filter. Must be either "group" or "private".
    :return: Decorator function that decorators the handler based on the chat type.
    """
    check_chat_type(chat_type)

    def decorator(handler: HandlerType) -> HandlerType:
        def handler_wrapper(notification: Notification) -> Any:
            for_group_chat = chat_type == "group" and is_group_chat(notification.chat)
            for_private_chat = chat_type == "private" and is_private_chat(
                notification.chat
            )

            condition = for_group_chat or for_private_chat

            return condition and handler(notification)

        return handler_wrapper

    return decorator
