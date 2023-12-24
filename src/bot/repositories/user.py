from sqlite3 import Connection, IntegrityError
from sqlite3 import Row

from bot.entities.user import User


class UserRepository:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.row_factory = Row

    def all(self) -> list[User]:
        stmt = "SELECT * FROM User"

        results = self.cursor.execute(stmt)

        return [User(**row) for row in results.fetchall()]

    def one(self, phone_number: str) -> User:
        stmt = "SELECT * FROM User WHERE phone_number = ?"

        result = self.cursor.execute(stmt, (phone_number,))

        return User(**result.fetchone())

    def exists(self, phone_number: str) -> bool:
        try:
            user = self.one(phone_number)

        except (IntegrityError, TypeError):
            return False

        else:
            return True

    def add(self, user: User) -> None:
        if self.exists(phone_number=user.phone_number):
            raise ValueError("User already exists")

        stmt = "INSERT INTO User (phone_number, username) VALUES (?, ?)"

        self.cursor.execute(stmt, (user.phone_number, user.username))
        self.connection.commit()

    def delete(self, phone_number: str) -> None:
        if self.exists(phone_number):
            stmt = "DELETE FROM User WHERE phone_number=(?)"

            self.cursor.execute(stmt, (phone_number,))
            self.connection.commit()

    def __del__(self) -> None:
        self.cursor.close()
        self.connection.close()
