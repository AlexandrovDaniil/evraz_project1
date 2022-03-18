from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import Chat, ChatMembers, ChatMessage, User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]:
        ...

    @abstractmethod
    def add_instance(self, user: User):
        ...

class ChatsRepo(ABC):
    @abstractmethod
    def get_by_id(self, chat_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def add_instance(self, chat: Chat):
        ...



class ChatsMembersRepo(ABC):
    @abstractmethod
    def add_instance(self, chat: Chat):
        ...

    # def update_info(self, chat: Chat):
    #     ...