from typing import List

import attr


@attr.dataclass
class User:
    id: int
    login: str
    password: str
    user_name: str



@attr.dataclass
class Chat:
    id: int
    chat_name: str
    author_id: User
    create_time: str
    update_time: str
    members_list: List["ChatMembers"] = attr.ib(factory=list)
    message_list: List["ChatMessage"] = attr.ib(factory=list)



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

