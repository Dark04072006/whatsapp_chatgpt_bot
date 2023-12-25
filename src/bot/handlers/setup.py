from whatsapp_chatbot_python.manager.router import Router

from bot.core.settings import ADMIN
from bot.handlers.commands import (
    clear_chat_history_list_users,
    clear_current_user_chat_history,
    clear_all_users_chat_history,
)
from bot.handlers.commands import (
    start_command,
    help_command,
    chatgpt_communicate_in_group,
    clear_chat_history,
)
from bot.handlers.messages import chatgpt_communicate


def register_handlers(router: Router) -> None:
    # standard commands for all users
    router.message.add_handler(start_command, command="start")
    router.message.add_handler(help_command, command="help")
    router.message.add_handler(clear_chat_history, command="clear")
    router.message.add_handler(chatgpt_communicate_in_group, command="chat")

    # only for admin commands
    router.message.add_handler(
        clear_chat_history_list_users, from_sender=ADMIN, command="clear_many"
    )
    router.message.add_handler(
        clear_current_user_chat_history, from_sender=ADMIN, command="clear_one"
    )
    router.message.add_handler(
        clear_all_users_chat_history, from_sender=ADMIN, command="clear_all"
    )

    # standard message text handlers
    router.message.add_handler(
        chatgpt_communicate,
        type_message=("textMessage", "extendedTextMessage"),
    )
