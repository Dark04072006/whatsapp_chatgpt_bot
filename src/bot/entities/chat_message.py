from dataclasses import dataclass

from bot.value_objects.role import Role


@dataclass(frozen=True)
class ChatMessage:
    role: Role
    content: str
