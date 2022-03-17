from classic.components import component
# from classic.http_auth import (
#     authenticate,
#     authenticator_needed,
#     authorize,
# )

from chat.application import services


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
