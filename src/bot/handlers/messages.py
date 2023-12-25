from openai import RateLimitError
from whatsapp_chatbot_python import Notification

from bot.core.container import chatgpt_communicator
from bot.decorators.chat_type import only_for_chat_type
from bot.entities.chat_message import ChatMessage


@only_for_chat_type(chat_type="private")
def chatgpt_communicate(notification: Notification) -> None:
    chat_message = ChatMessage(
        role="user",
        content=notification.message_text,
        user_id=notification.sender,
    )

    try:
        chatgpt_answer = chatgpt_communicator.get_chatgpt_answer(
            chat_message=chat_message
        )

    except RateLimitError:
        notification.answer(
            "Слишком много запросов. Попробуйте через минуту, пожалуйста."
        )

    else:
        notification.answer(chatgpt_answer)
