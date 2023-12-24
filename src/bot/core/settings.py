import logging
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

logging.basicConfig(level=logging.INFO)


# proxy constants
PROXY: str = getenv("PROXY")

# openai constants
OPENAI_API_KEY: str = getenv("OPENAI_API_KEY")

# whatsapp bot constants
ADMIN: str = getenv("ADMIN")
ID_INSTANCE: str = getenv("ID_INSTANCE")
API_TOKEN_INSTANCE: str = getenv("API_TOKEN_INSTANCE")

# database constants
DATABASE_URI: Path = BASE_DIR / getenv("SQLITE_DB_PATH")
