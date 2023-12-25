import logging

from bot.core.whatsapp_bot import whatsapp_bot

logger = logging.getLogger(__name__)


def main() -> None:
    whatsapp_bot.run_forever()


if __name__ == "__main__":
    main()
