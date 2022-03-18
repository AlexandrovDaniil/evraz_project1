from typing import List, Optional, Tuple

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import conint, validate_arguments

from . import errors, interfaces
from .dataclasses import Chat, ChatMembers, ChatMessage, User

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


class ChatUpdateInfo(DTO):
    author_id: int
    chat_name: str = None
    description: str = None
    creation_date: str = None
    id: int = None


class AddChatMember(DTO):
    user_id: int
    chat_id: int
    alive: Optional[str] = None
    banned: Optional[str] = None


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
    user_repo: interfaces.UsersRepo
    chat_members_repo: interfaces.ChatsMembersRepo

    def user_check(self, user_id):
        if self.user_repo.get_by_id(user_id):
            return True
        raise Exception(f'User with id: {user_id} does not exist')

    def chat_check(self, chat_id):
        if self.chat_repo.get_by_id(chat_id):
            return True
        raise errors.NoChat(id=chat_id)

    def author_check(self, user_id, chat_id):
        chat = self.chat_repo.get_by_id(chat_id)
        if chat.author_id == user_id:
            return True
        raise errors.NoAuthor(id=user_id)

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
        if self.user_check(chat_info.author_id):
            new_chat = chat_info.create_obj(Chat)
            chat_id = self.chat_repo.add_instance(new_chat)
            add_author = AddChatMember(user_id=chat_info.author_id, chat_id=chat_id)
            self.add_user(**add_author.dict())

    @join_point
    @validate_with_dto
    def update_chat(self, chat_info: ChatUpdateInfo):
        chat = self.chat_repo.get_by_id(chat_info.id)
        if chat and self.author_check(user_id=chat_info.author_id, chat_id=chat_info.id):
            chat_info.populate_obj(chat)

    @join_point
    @validate_with_dto
    def add_user(self, chat_members_info: AddChatMember):
        if self.chat_check(chat_members_info.chat_id) and self.user_check(chat_members_info.user_id):
            new_chat_member = chat_members_info.create_obj(ChatMembers)
            self.chat_members_repo.add_instance(new_chat_member)


