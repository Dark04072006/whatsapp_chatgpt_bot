from sqlite3 import Connection, Row

from bot.entities.chat_message import ChatMessage


class ChatRepository:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.row_factory = Row

    def all_messages(self) -> list[ChatMessage]:
        stmt = "SELECT * FROM ChatMessage"

        rows = self.cursor.execute(stmt)

        return [
            ChatMessage(
                role=row["role"],
                content=row["content"],
            )
            for row in rows.fetchall()
        ]

    def all_user_messages(self, user_number: str) -> list[ChatMessage]:
        stmt = "SELECT * FROM ChatMessage WHERE user_number = ?"

        rows = self.cursor.execute(stmt, (user_number,))

        return [
            ChatMessage(
                role=row["role"],
                content=row["content"],
            )
            for row in rows.fetchall()
        ]

    def add_user_message(self, user_number: str, message: ChatMessage) -> None:
        stmt = "INSERT INTO ChatMessage (user_number, role, content) VALUES (?, ?, ?)"

        self.cursor.execute(stmt, (user_number, message.role, message.content))

    def exists_user_messages(self, user_number: str) -> bool:
        stmt = "SELECT * FROM ChatMessage WHERE user_number = ? LIMIT 1"

        row = self.cursor.execute(stmt, (user_number,))

        return bool(row.fetchone())

    def delete_user_messages(self, user_number: str) -> None:
        if self.exists_user_messages(user_number):
            stmt = "DELETE FROM ChatMessage WHERE user_number = ?"

            self.cursor.execute(stmt, (user_number,))

    def delete_all_messages(self) -> None:
        self.cursor.execute("DELETE FROM ChatMessage")

    def __del__(self) -> None:
        self.cursor.close()
        self.connection.close()
