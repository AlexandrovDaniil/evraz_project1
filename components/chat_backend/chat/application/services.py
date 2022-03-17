from typing import List, Optional, Tuple

from pydantic import conint, validate_arguments

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component


from . import errors, interfaces
from .dataclasses import User, ChatMembers, ChatMessage, Chat

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: int
    login: str
    password: str
    user_name: str


@component
class Users:
    user_repo: interfaces.UsersRepo

    @join_point
    #@validate_arguments
    def get_info(self, user_id: int):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise errors.NoUser(id=user_id)
        return user

