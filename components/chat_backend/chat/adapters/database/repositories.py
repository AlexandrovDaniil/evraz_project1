from typing import List, Optional

from chat.application import interfaces
from chat.application.dataclasses import Chat, ChatMembers, ChatMessage, User
from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):
    def get_by_id(self, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        return self.session.execute(query).scalars().one_or_none()

    def add_instance(self, user: User):
        self.session.add(user)
        self.session.flush()



@component
class ChatsRepo(BaseRepository, interfaces.ChatsRepo):
    def get_by_id(self, chat_id: int) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == chat_id)
        return self.session.execute(query).scalars().one_or_none()

    def add_instance(self, chat: Chat):
        self.session.add(chat)
        self.session.flush()
        return chat.id


@component
class ChatsMembersRepo(BaseRepository, interfaces.ChatsMembersRepo):

    def add_instance(self, chat_members: ChatMembers):
        self.session.add(chat_members)
        self.session.flush()
