from typing import Tuple, Union

import falcon

from classic.http_api import App
from classic.http_auth import Authenticator
from classic.http_auth import strategies as auth_strategies

from chat.application import services

from . import auth, controllers


def create_app(
    is_dev_mode: bool,
    allow_origins: Union[str, Tuple[str, ...]],
    users: services.Users,
    chats: services.Chats,
) -> App:


    app = App(prefix='/api')
    app.register(controllers.Users(users=users))
    app.register(controllers.Chats(chats=chats))


    return app
