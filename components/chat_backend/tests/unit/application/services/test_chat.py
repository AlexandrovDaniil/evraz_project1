from datetime import datetime

import pytest
from attr import asdict
from chat.application.services import Chats, Users


@pytest.fixture(scope='function')
def service_user(user_repo):
    return Users(user_repo=user_repo)


@pytest.fixture(scope='function')
def service_chat(user_repo, chat_repo, chat_members_repo, chat_messages_repo):
    return Chats(user_repo=user_repo, chat_repo=chat_repo, chat_members_repo=chat_members_repo,
                 chat_messages_repo=chat_messages_repo)


data_user = {

    'login': 'user_login_1',
    'password': 'user_password_1',
    'user_name': 'user_name_1',
    'id': 1,
}

data_chat = {
    'author_id': 1,
    'chat_name': 'chat_1',
    'description': 'desc_1',
    'creation_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
    'id': 1
}

data_chat_update = {
    'author_id': 1,
    'chat_name': 'chat_new',
    'description': 'desc_new',
    'creation_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
    'id': 1
}

data_chat_user = {
    'chat_id': 1,
    'user_id': 1,
    'author_id': 1,
    'id': 1,
}

data_chat_msg = {
    'chat_id': 1,
    'user_id': 1,
    'text': 'my msg',
    'id': 1,
    'send_time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
}


def test_add_user(service_user):
    service_user.add_user(**data_user)
    service_user.user_repo.add_instance.assert_called_once()


def test_get_user(service_user, user_repo):
    user = service_user.get_info(id=1)
    assert asdict(user) == data_user


def test_add_chat(service_chat):
    service_chat.add_chat(**data_chat)
    service_chat.chat_repo.add_instance.assert_called_once()


def test_update_chat(service_chat):
    new_chat = service_chat.update_chat(**data_chat_update)
    assert asdict(new_chat) == data_chat_update


def test_get_chat(service_chat):
    chat = service_chat.get_info(chat_id=1, user_id=1)
    assert asdict(chat) == data_chat


def test_add_chat_user(service_chat):
    service_chat.add_user(**data_chat_user)
    service_chat.chat_members_repo.add_instance.assert_called_once()


def test_add_chat_msg(service_chat):
    service_chat.send_massage(**data_chat_msg)
    service_chat.chat_messages_repo.send_message.assert_called_once()


def test_delete_chat(service_chat):
    service_chat.delete_chat(chat_id=1, user_id=1)
    service_chat.chat_repo.delete_instance.assert_called_once()


def test_leave(service_chat):
    service_chat.leave_chat(chat_id=1, user_id=1)
    service_chat.chat_repo.delete_instance.assert_called_once()


def test_get_chat_user(service_chat):
    members = service_chat.get_users(chat_id=1, user_id=1)
    assert asdict(members) == data_chat_user


def test_get_chat_msg(service_chat):
    messages = service_chat.get_message(chat_id=1, user_id=1)
    assert asdict(messages) == data_chat_msg
