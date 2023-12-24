import logging

from bot.core.container import whatsapp_bot
from bot.handlers.setup import register_handlers

logger = logging.getLogger(__name__)


def main() -> None:
    register_handlers(bot=whatsapp_bot)

    whatsapp_bot.run_forever()


if __name__ == "__main__":
    main()
