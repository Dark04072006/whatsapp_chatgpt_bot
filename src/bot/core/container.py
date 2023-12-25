from httpx import Client
from openai import OpenAI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bot.core.settings import (
    OPENAI_API_KEY,
    PROXY,
    DATABASE_URI,
)
from bot.managers.chat_history import ChatHistoryManager
from bot.models import BaseOrmModel
from bot.services import ChatGPTCommunicationService
from bot.uow import UnitOfWork

database_engine = create_engine(DATABASE_URI)

BaseOrmModel.metadata.create_all(database_engine)
session_maker = sessionmaker(bind=database_engine)

uow = UnitOfWork(session_maker)

http_client = Client(proxy=PROXY)
openai_client = OpenAI(api_key=OPENAI_API_KEY, http_client=http_client)
chatgpt_communicator = ChatGPTCommunicationService(openai_client=openai_client, uow=uow)
chat_history_manager = ChatHistoryManager(uow=uow)
