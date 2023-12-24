from bot.core.container import chatgpt_communicator, chat_history_manager
from bot.decorators.chat_type import only_for_chat_type
from bot.decorators.transaction import transaction
from bot.entities.chat_message import ChatMessage
from openai import RateLimitError
from whatsapp_chatbot_python import Notification


@only_for_chat_type(chat_type="group")
def chatgpt_communicate_in_group(notification: Notification) -> None:
    _, prompt = notification.message_text.split(maxsplit=1)

    chat_message = ChatMessage(role="user", content=prompt)

    try:
        chatgpt_answer = chatgpt_communicator.get_chatgpt_answer(
            user_number=notification.sender, chat_message=chat_message
        )

    except RateLimitError:
        notification.answer(
            "Слишком много запросов. Попробуйте через минуту, пожалуйста.",
            notification.event["idMessage"],
        )

    else:
        notification.answer(chatgpt_answer, notification.event["idMessage"])


@transaction
def clear_chat_history(notification: Notification) -> None:
    chat_history_manager.delete_user_chat_history(notification.sender)

    notification.answer("Диалог был удален по просьбе пользователя.")
