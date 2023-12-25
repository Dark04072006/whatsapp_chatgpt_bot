from bot.middlewares.add_user import add_user_middleware
from bot.router import MyRouter


def register_middlewares(router: MyRouter) -> None:
    router.add_middleware(add_user_middleware)
