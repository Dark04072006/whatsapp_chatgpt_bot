from typing import Callable, Any

from whatsapp_chatbot_python.manager.router import Router


class MyRouter(Router):
    middlewares = []

    def route_event(self, event: dict[str, Any]) -> None:
        for middleware in self.middlewares:
            middleware(event)

        super().route_event(event)

    def add_middleware(self, middleware: Callable[[dict[str, Any]], None]) -> None:
        self.middlewares.append(middleware)
