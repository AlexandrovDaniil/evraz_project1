from classic.components import component
# from classic.http_auth import (
#     authenticate,
#     authenticator_needed,
#     authorize,
# )

from chat.application import services
from falcon import Request, Response

from .join_points import join_point


#@authenticator_needed
@component
class Users:
    users: services.Users

    @join_point
    def on_get_show_info(self, request, response):

        users = self.users.get_info(**request.params)

        response.media = {
            'user_id': users.id,
            'login': users.login,
            'user_name': users.user_name
        }

    @join_point
    def on_post_add_user(self, request: Request, response: Response):
        print(request.media)
        self.users.add_user(**request.media)


@component
class Chats:
    chats: services.Chats

    @join_point
    def on_get_show_info(self, request, response):

        chats = self.chats.get_info(**request.params)

        response.media = {
            'chat_id': chats.id,
            'title': chats.chat_name,
            'description': chats.description,
            'author_id': chats.author_id
        }

    @join_point
    def on_post_add_chat(self, request: Request, response: Response):
        print(request.media)
        self.chats.add_chat(**request.media)