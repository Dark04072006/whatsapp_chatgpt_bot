from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    phone_number: str
    username: str
