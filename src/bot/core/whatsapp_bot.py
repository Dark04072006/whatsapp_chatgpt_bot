from whatsapp_chatbot_python import GreenAPIBot

from bot.core.settings import ID_INSTANCE, API_TOKEN_INSTANCE
from bot.handlers.setup import register_handlers
from bot.middlewares.setup import register_middlewares
from bot.router import MyRouter

whatsapp_bot = GreenAPIBot(
    id_instance=ID_INSTANCE,
    api_token_instance=API_TOKEN_INSTANCE,
    delete_notifications_at_startup=False,
)
whatsapp_bot.router = MyRouter(whatsapp_bot.api, whatsapp_bot.logger)

register_handlers(router=whatsapp_bot.router)
register_middlewares(router=whatsapp_bot.router)
