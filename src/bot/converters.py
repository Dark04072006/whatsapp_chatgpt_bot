from dataclasses import asdict

from bot.entities.chat_message import ChatMessage


def chat_message_objects_list_to_list_of_dictionaries(
    message_list: list[ChatMessage],
) -> list[dict[str, str]]:
    return [asdict(message) for message in message_list]
