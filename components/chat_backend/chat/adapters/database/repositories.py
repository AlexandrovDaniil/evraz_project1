from typing import List, Optional

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from chat.application import interfaces
from chat.application.dataclasses import User, ChatMembers, ChatMessage, Chat


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):
    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()
