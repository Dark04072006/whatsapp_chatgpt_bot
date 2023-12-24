from sqlite3 import Connection

from bot.core.settings import (
    OPENAI_API_KEY,
    PROXY,
    ID_INSTANCE,
    API_TOKEN_INSTANCE,
    DATABASE_URI,
)
from bot.managers.chat_history import ChatHistoryManager
from bot.repositories import (
    UserRepository,
    ChatRepository,
)
from bot.services import ChatGPTCommunicationService
from httpx import Client
from openai import OpenAI
from whatsapp_chatbot_python import GreenAPIBot

database_connection = Connection(DATABASE_URI)
user_repository = UserRepository(connection=database_connection)
chat_repository = ChatRepository(connection=database_connection)

http_client = Client(proxy=PROXY)
openai_client = OpenAI(api_key=OPENAI_API_KEY, http_client=http_client)
chatgpt_communicator = ChatGPTCommunicationService(
    openai_client=openai_client, chat_repository=chat_repository
)
chat_history_manager = ChatHistoryManager(chat_repository=chat_repository)

whatsapp_bot = GreenAPIBot(
    id_instance=ID_INSTANCE,
    api_token_instance=API_TOKEN_INSTANCE,
)
