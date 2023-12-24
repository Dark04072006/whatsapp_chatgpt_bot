import logging

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        from bot.core.container import whatsapp_bot
        from bot.handlers.setup import register_handlers

        register_handlers(bot=whatsapp_bot)
        whatsapp_bot.run_forever()
        logger.log(logging.INFO, "Бот завершил работу.")

    except KeyboardInterrupt:
        logger.log(logging.INFO, "Бот остановлен пользователем.")
