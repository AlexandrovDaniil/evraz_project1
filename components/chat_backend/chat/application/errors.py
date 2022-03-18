from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "No user with id '{id}'"
    code = 'chat.no_user'

class NoChat(AppError):
    msg_template = "No chat with id '{id}'"
    code = 'chat.no_chat'

class NoAuthor(AppError):
    msg_template = "User with id '{id}' is not author of this chat"
    code = 'chat.no_author'