from typing import List, Optional
from datetime import datetime
import attr


@attr.dataclass
class User:
    login: str
    password: str
    user_name: str


@attr.dataclass
class Chat:
    author_id: 'User'
    chat_name: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[str] = attr.ib(factory=lambda: str(datetime.utcnow()))
    id: Optional[int] = None


@attr.dataclass
class ChatMessage:
    chat_id: 'Chat'
    user_id: 'User'
    text: str
    send_time: str
    id: Optional[int] = None


@attr.dataclass
class ChatMembers:
    chat_id: 'Chat'
    user_id: 'User'
    alive: str
    banned: str
    id: Optional[int] = None
