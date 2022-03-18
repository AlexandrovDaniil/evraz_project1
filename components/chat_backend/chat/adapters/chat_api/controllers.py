from chat.application import services
from classic.components import component

from .join_points import join_point


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
    def on_post_add_user(self, request, response):
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
    def on_post_add_chat(self, request, response):
        self.chats.add_chat(**request.media)

    @join_point
    def on_post_update_chat(self, request, response):
        self.chats.update_chat(**request.media)

    @join_point
    def on_post_add_user(self, request, response):
        self.chats.add_user(**request.media)

    @join_point
    def on_post_send_message(self, request, response):
        self.chats.send_massage(**request.media)

    @join_point
    def on_get_get_users(self, request, response):
        users = self.chats.get_users(**request.params)
        response.media = {'users': users}

    @join_point
    def on_get_get_messages(self, request, response):
        messages = self.chats.get_message(**request.params)
        response.media = {message.send_time: message.text for message in messages}


