from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import User, ChatMembers, ChatMessage, Chat


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[User]:
        ...



