from sqlalchemy import create_engine
from classic.sql_storage import TransactionContext
from chat.adapters import database, chat_api
from chat.application import services


class Settings:
    db = database.Settings()
    chat_api = chat_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)
    chats_repo = database.repositories.ChatsRepo(context=context)


class Application:
    users = services.Users(user_repo=DB.users_repo)
    chats = services.Chats(chat_repo=DB.chats_repo)
    is_dev_mode = Settings.chat_api.IS_DEV_MODE
    allow_origins = Settings.chat_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    chat_api.join_points.join(DB.context)


app = chat_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    users=Application.users,
    chats=Application.chats,
)
