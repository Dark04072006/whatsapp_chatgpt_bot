from whatsapp_chatbot_python import Notification


def start_command(notification: Notification) -> None:
    sender_name: str = notification.event["senderData"]["senderName"]

    notification.answer(
        f"Привет, *{sender_name}*.\n"
        f"Для получения доп. информации воспользуйся "
        f"командой /help.\nИтак, задай нужный тебе "
        f"вопрос и я на него отвечу.",
        notification.event["idMessage"],
    )


def help_command(notification: Notification) -> None:
    notification.answer(
        "Тут особо объяснять нечего. "
        "Просто пишешь нужный тебе вопрос и "
        "получаешь ответ.\n"
        "Список команд:\n"
        "1) /start - запуск бота\n"
        "2) /help - список команд\n"
        "3) /chat - команда для групповых"
        " чатов, используется в следующем формате: "
        "/chat пользовательский запрос\n"
        "4) /clear - удалить диалог с ChatGPT",
    )
