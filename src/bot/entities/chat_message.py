from dataclasses import dataclass

from bot.value_objects.message_role import MessageRole


@dataclass(frozen=True)
class ChatMessage:
    role: MessageRole
    content: str
    user_id: str
