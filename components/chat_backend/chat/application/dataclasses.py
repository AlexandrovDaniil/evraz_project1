from typing import List, Optional
from datetime import datetime
import attr


@attr.dataclass
class User:
    login: str
    password: str
    user_name: str
    id: Optional[int] = None


@attr.dataclass
class Chat:

    author_id: User
    chat_name: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[str] = attr.ib(factory=lambda: str(datetime.now()))
    id: Optional[int] = None
    # members_list: List["ChatMembers"] = attr.ib(factory=list)
    # message_list: List["ChatMessage"] = attr.ib(factory=list)


@attr.dataclass
class ChatMessage:
    id: int
    chat_id: Chat
    user_id: User
    text: str
    send_time: str


@attr.dataclass
class ChatMembers:
    id: int
    chat_id: Chat
    user_id: User
    alive: str
    banned: str
