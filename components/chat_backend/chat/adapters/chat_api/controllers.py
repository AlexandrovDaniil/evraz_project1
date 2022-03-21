import jwt

from chat.application import services
from classic.components import component
from classic.http_auth import authenticate, authenticator_needed

from .join_points import join_point


@authenticator_needed
@component
class Users:
    users: services.Users

    def generate_token(self, user) -> str:
        token = jwt.encode({
            'sub': user.id,
            'login': user.login,
            'name': user.user_name,
            'group': 'User'

        }, 'my_secret_jwt', algorithm='HS256')
        return token

    @join_point
    @authenticate
    def on_get_show_info(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        users = self.users.get_info(**request.params)
        response.media = {
            'user_id': users.id,
            'login': users.login,
            'user_name': users.user_name
        }

    @join_point
    def on_post_add_user(self, request, response):
        user = self.users.add_user(**request.media)
        token = self.generate_token(user)
        response.media = token

    @join_point
    def on_post_user_login(self, request, response):
        user = self.users.login_user(**request.media)
        token = self.generate_token(user)
        response.media = token


@authenticator_needed
@component
class Chats:
    chats: services.Chats

    @authenticate
    @join_point
    def on_get_show_info(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        chats = self.chats.get_info(**request.params)
        response.media = {
            'chat_id': chats.id,
            'title': chats.chat_name,
            'description': chats.description,
            'author_id': chats.author_id
        }

    @authenticate
    @join_point
    def on_post_add_chat(self, request, response):
        request.media['author_id'] = request.context.client.user_id
        self.chats.add_chat(**request.media)

    @authenticate
    @join_point
    def on_post_update_chat_info(self, request, response):
        request.media['author_id'] = request.context.client.user_id
        self.chats.update_chat(**request.media)

    @authenticate
    @join_point
    def on_post_add_user(self, request, response):
        request.media['author_id'] = request.context.client.user_id
        self.chats.add_user(**request.media)

    @authenticate
    @join_point
    def on_post_send_message(self, request, response):
        request.media['user_id'] = request.context.client.user_id
        self.chats.send_massage(**request.media)

    @authenticate
    @join_point
    def on_get_get_users(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        users = self.chats.get_users(**request.params)
        response.media = {'users': [user.user_name for user in users]}

    @authenticate
    @join_point
    def on_get_get_messages(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        messages = self.chats.get_message(**request.params)
        response.media = {message.send_time: message.text for message in messages}

    @authenticate
    @join_point
    def on_post_delete_chat(self, request, response):
        request.media['user_id'] = request.context.client.user_id
        self.chats.delete_chat(**request.media)

    @authenticate
    @join_point
    def on_post_leave(self, request, response):
        request.media['user_id'] = request.context.client.user_id
        self.chats.leave(**request.media)
