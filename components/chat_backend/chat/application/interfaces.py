from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import User, ChatMembers, ChatMessage, Chat


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

