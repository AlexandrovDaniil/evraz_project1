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
        result = self.session.execute(query).scalars().one_or_none()
        return result

    def add_instance(self, user: User):
        self.session.add(user)
        self.session.flush()


@component
class ChatsRepo(BaseRepository, interfaces.ChatsRepo):
    def get_by_id(self, chat_id: int, user_id: Optional[int] = None) -> Optional[Chat]:
        query = select(Chat).where(Chat.id == chat_id)
        return self.session.execute(query).scalars().one_or_none()

    def add_instance(self, chat: Chat):
        self.session.add(chat)
        self.session.flush()
        return chat.id

    def delete_instance(self, chat: Chat):
        members = self.session.query(ChatMembers).where(ChatMembers.chat_id == chat.id).all()
        [self.session.delete(member) for member in self.session.query(ChatMembers).where(
            ChatMembers.chat_id == chat.id).all()]
        self.session.commit()

        self.session.delete(chat)
        self.session.commit()


@component
class ChatsMembersRepo(BaseRepository, interfaces.ChatsMembersRepo):
    def add_instance(self, chat_members: ChatMembers):
        self.session.add(chat_members)
        self.session.flush()

    def get_users(self, chat_id: int, user_id: Optional[int] = None) -> List[User]:
        query = self.session.query(User, ChatMembers)
        query = query.join(User, User.id == ChatMembers.user_id)
        query = query.filter(ChatMembers.chat_id == chat_id)
        records = self.session.execute(query).scalars().all()
        return records


@component
class ChatsMessagesRepo(BaseRepository, interfaces.ChatsMessagesRepo):
    def send_message(self, message: ChatMessage):
        self.session.add(message)
        self.session.flush()

    def get_message(self, chat_id: int, user_id: Optional[int] = None) -> Optional[List[ChatMessage]]:
        query = select(ChatMessage).where(ChatMessage.chat_id == chat_id)
        records = self.session.execute(query).scalars().all()
        return records
