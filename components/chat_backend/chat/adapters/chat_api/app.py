from typing import Tuple, Union
from classic.http_api import App
from chat.application import services
from . import controllers


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
