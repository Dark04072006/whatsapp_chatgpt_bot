from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from bot.converters import user_model_to_user_entity, user_entity_to_user_model
from bot.entities.user import User
from bot.models.user import UserOrmModel


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self) -> list[User]:
        users = self.session.query(UserOrmModel).all()

        converted = map(user_model_to_user_entity, users)

        return list(converted)

    def one(self, whatsapp_id: str) -> User:
        user = (
            self.session.query(UserOrmModel)
            .where(UserOrmModel.whatsapp_id == whatsapp_id)
            .one()
        )

        return user_model_to_user_entity(user)

    def exists(self, whatsapp_id: str) -> bool:
        return self.session.scalar(
            exists().where(UserOrmModel.whatsapp_id == whatsapp_id).select()
        )

    def add(self, user: User) -> None:
        if self.exists(whatsapp_id=user.whatsapp_id):
            raise ValueError("User already exists")

        user_orm_model = user_entity_to_user_model(user)

        self.session.add(user_orm_model)

    def delete_where(self, whatsapp_id: str) -> None:
        if self.exists(whatsapp_id=whatsapp_id):
            self.session.query(UserOrmModel).delete()
