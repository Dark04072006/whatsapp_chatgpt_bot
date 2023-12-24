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
from whatsapp_chatbot_python import GreenAPIBot


def register_handlers(bot: GreenAPIBot) -> None:
    # standard commands for all users
    bot.router.message.add_handler(start_command, command="start")
    bot.router.message.add_handler(help_command, command="help")
    bot.router.message.add_handler(clear_chat_history, command="clear")
    bot.router.message.add_handler(chatgpt_communicate_in_group, command="chat")

    # only for admin commands
    bot.router.message.add_handler(
        clear_chat_history_list_users, from_sender=ADMIN, command="clear_many"
    )
    bot.router.message.add_handler(
        clear_current_user_chat_history, from_sender=ADMIN, command="clear_one"
    )
    bot.router.message.add_handler(
        clear_all_users_chat_history, from_sender=ADMIN, command="clear_all"
    )

    # standard message text handlers
    bot.router.message.add_handler(
        chatgpt_communicate,
        type_message=("textMessage", "extendedTextMessage"),
    )
