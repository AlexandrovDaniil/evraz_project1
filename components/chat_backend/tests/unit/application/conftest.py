from unittest.mock import Mock

import pytest

from chat.application import interfaces, dataclasses

@pytest.fixture(scope='function')
def users():
    return dataclasses.User(

        user_name='User3',
        login='login3',
        password='password3',
        id = 1,
    )

@pytest.fixture(scope='function')
def users_repo111(users):
    users_repo1 = Mock(interfaces.UsersRepo)
    users_repo1.get_by_user_id = Mock(return_value=users)
    return users_repo1