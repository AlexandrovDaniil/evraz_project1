from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "No user with id '{id}'"
    code = 'chat.no_user'

class NoUserLogin(AppError):
    msg_template = "No user with login '{login}'"
    code = 'chat.no_user_login'

class WrongUserPassword(AppError):
    msg_template = "Wrong password"
    code = 'chat.wrong_password'

class NoChat(AppError):
    msg_template = "No chat with id '{id}'"
    code = 'chat.no_chat'

class NoAuthor(AppError):
    msg_template = "User with id '{id}' is not author of this chat"
    code = 'chat.no_author'

class NoUserInChat(AppError):
    msg_template = "User with id '{id}' is not in this chat"
    code = 'chat.no_user_in_chat'