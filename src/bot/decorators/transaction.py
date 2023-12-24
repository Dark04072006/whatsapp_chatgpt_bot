import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)


def transaction(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        from bot.core.container import database_connection

        try:
            call = func(*args, **kwargs)

        except Exception as e:
            database_connection.rollback()
            logger.exception(e)

        else:
            database_connection.commit()
            return call

    return wrapper
