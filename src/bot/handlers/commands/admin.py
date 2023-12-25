from whatsapp_chatbot_python import Notification

from bot.core.container import chat_history_manager


def clear_chat_history_list_users(notification: Notification) -> None:
    _, *list_user_ids = notification.message_text.split()

    if len(list_user_ids) < 2:
        notification.answer("Количество удаляемых чатов должно быть от двух и более.")

    else:
        chat_history_manager.delete_users_chat_history(list_user_ids)

        answer = f"Просьба администратора удалить диалоги с пользователями: {' '.join(list_user_ids)} выполнена."

        notification.answer(answer, notification.event["idMessage"])


def clear_current_user_chat_history(notification: Notification) -> None:
    _, *entities = notification.message_text.split()

    if len(entities) > 1:
        notification.answer(
            "Удалить чат с помощью данной команды можно только одному пользователю"
        )

    else:
        user_number = entities[0]

        chat_history_manager.delete_user_chat_history(notification.sender)

        answer = (
            f"Просьба администратора удалить "
            f"диалог с пользователем: {user_number} выполнена"
        )

        notification.answer(answer, notification.event["idMessage"])


def clear_all_users_chat_history(notification: Notification) -> None:
    chat_history_manager.delete_all_chat_history()

    notification.answer(
        "Просьба администратора удалить диалоги с пользователями выполнена."
    )
