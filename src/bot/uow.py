from contextlib import contextmanager
from typing import ContextManager, TypeVar, Generic

from sqlalchemy.orm import sessionmaker, Session

Repository = TypeVar("Repository")


class UnitOfWork(Generic[Repository]):
    def __init__(self, session_maker: sessionmaker[Session]) -> None:
        self.session_maker = session_maker

    @contextmanager
    def __call__(self, repository: Repository) -> ContextManager["UnitOfWork"]:
        self.session = self.session_maker()

        self.repository: Repository = repository(self.session)

        yield self

        self.session.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
