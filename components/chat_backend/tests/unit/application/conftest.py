from datetime import datetime
from unittest.mock import Mock

import pytest
from chat.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def user():
    return dataclasses.User(
        user_name='user_name_1',
        login='user_login_1',
        password='user_password_1',
        id=1,
    )


@pytest.fixture(scope='function')
def chat():
    return dataclasses.Chat(
        author_id=1,
        chat_name='chat_1',
        description='desc_1',
        id=1,
        creation_date=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    )


@pytest.fixture(scope='function')
def chat_members():
    return dataclasses.ChatMembers(
        chat_id=1,
        user_id=1,
        author_id=1,
        id=1
    )


@pytest.fixture(scope='function')
def chat_messages():
    return dataclasses.ChatMessage(
        chat_id=1,
        user_id=1,
        text='my msg',
        id=1,
        send_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    )


@pytest.fixture(scope='function')
def user_repo(user):
    user_repo = Mock(interfaces.UsersRepo)
    user_repo.get_by_id = Mock(return_value=user)
    user_repo.add_instance = Mock(return_value=user)
    return user_repo


@pytest.fixture(scope='function')
def chat_repo(chat):
    chat_repo = Mock(interfaces.ChatsRepo)
    chat_repo.get_by_id = Mock(return_value=chat)
    chat_repo.add_instance = Mock(return_value=chat)
    return chat_repo


@pytest.fixture(scope='function')
def chat_messages_repo(chat_messages):
    chat_messages_repo = Mock(interfaces.ChatsMessagesRepo)
    chat_messages_repo.get_message = Mock(return_value=chat_messages)
    return chat_messages_repo


@pytest.fixture(scope='function')
def chat_members_repo(chat_members):
    chat_members_repo = Mock(interfaces.UsersRepo)
    chat_members_repo.get_users = Mock(return_value=chat_members)
    chat_members_repo.leave = Mock(return_value=chat_members)
    return chat_members_repo
