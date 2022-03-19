import pytest
from attr import asdict

from chat.application import services


@pytest.fixture(scope='function')
def service_user(users_repo111):
    return services.Users(user_repo=users_repo111)


data_user = {
    'id': 1,
    'user_name': 'User3',
    'login': 'login3',
    'password': 'password3'
}


def test_add_user(service_user):
    service_user.add_user(**data_user)
    service_user.user_repo.add_instance.assert_called_once()


def test_get_user(service_user):
    user = service_user.get_info(user_id=1)
    print(user)
    assert asdict(user) == data_user
