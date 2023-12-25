from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.models.base import BaseOrmModel

if TYPE_CHECKING:
    from bot.models.message import MessageOrmModel


class UserOrmModel(BaseOrmModel):
    __tablename__ = "users"

    role: Mapped[str]
    username: Mapped[str]
    whatsapp_id: Mapped[str] = mapped_column(primary_key=True)
    messages: Mapped["MessageOrmModel"] = relationship(back_populates="user")
