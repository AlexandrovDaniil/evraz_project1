from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import Chat, ChatMembers, ChatMessage, User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]: ...

    @abstractmethod
    def add_instance(self, user: User): ...


class ChatsRepo(ABC):
    @abstractmethod
    def get_by_id(self, chat_id: int) -> Optional[Chat]: ...

    @abstractmethod
    def add_instance(self, chat: Chat): ...

    @abstractmethod
    def delete_instance(self, chat_id: int): ...


class ChatsMembersRepo(ABC):
    @abstractmethod
    def add_instance(self, chat: ChatMembers): ...

    @abstractmethod
    def get_users(self, chat_id: int) -> Optional[User]: ...


class ChatsMessagesRepo(ABC):
    @abstractmethod
    def send_message(self, message: ChatMessage): ...

    @abstractmethod
    def get_message(self, chat_id: int) -> Optional[ChatMessage]: ...
