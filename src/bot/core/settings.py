import logging
from os import getenv
from pathlib import Path
from typing import List

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
DATABASE_URI = getenv("SQLITE_URI")

# debug mode
DEBUG: bool = True

SECRET_APP_KEY: str = getenv("SECRET_APP_KEY")
# webhook constants
ALLOWED_ORIGINS: List[str] = [
    "51.250.84.44",
    "51.250.94.65",
    "51.250.91.13",
    "51.250.93.251",
    "51.250.76.115",
    "51.250.69.65",
    "51.250.68.181",
    "51.250.69.45",
    "51.250.74.200",
    "51.250.87.205",
    "51.250.89.177",
    "64.226.125.75",
    "158.160.49.84",
]
