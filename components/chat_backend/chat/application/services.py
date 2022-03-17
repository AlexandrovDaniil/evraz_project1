from typing import List, Optional, Tuple

from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import User, ChatMembers, ChatMessage, Chat

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    login: str
    password: str
    user_name: str


class ChatInfo(DTO):
    author_id: int
    chat_name: Optional[str]
    description: Optional[str]
    creation_date: Optional[str]
    id: Optional[int]


@component
class Users:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        user = self.user_repo.get_by_id(id)
        if not user:
            raise errors.NoUser(id=id)
        return user

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        new_user = user_info.create_obj(User)
        self.user_repo.add_instance(new_user)


@component
class Chats:
    chat_repo: interfaces.ChatsRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        chat = self.chat_repo.get_by_id(id)
        if not chat:
            raise errors.NoChat(id=id)
        return chat

    @join_point
    @validate_with_dto
    def add_chat(self, chat_info: ChatInfo):
        new_chat = chat_info.create_obj(Chat)
        self.chat_repo.add_instance(new_chat)
