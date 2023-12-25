from dataclasses import dataclass

from bot.value_objects.user_role import UserRole


@dataclass(frozen=True)
class User:
    role: UserRole
    username: str
    whatsapp_id: str
