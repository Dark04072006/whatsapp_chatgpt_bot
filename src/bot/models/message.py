from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.models.base import BaseOrmModel

if TYPE_CHECKING:
    from bot.models.user import UserOrmModel


class MessageOrmModel(BaseOrmModel):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]
    content: Mapped[str]
    user: Mapped["UserOrmModel"] = relationship(back_populates="messages")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.whatsapp_id"))
