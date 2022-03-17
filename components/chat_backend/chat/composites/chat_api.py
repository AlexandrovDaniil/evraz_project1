from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from chat.adapters import database, chat_api
from chat.application import services


class Settings:
    db = database.Settings()
    chat_api = chat_api.Settings()


# class Logger:
#     log.configure(
#         Settings.db.LOGGING_CONFIG,
#         Settings.shop_api.LOGGING_CONFIG,
#     )


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)
    # conn = engine.connect()
    # user1 = database.user.insert().values(login='test1', password='testpass', user_name='qwe')
    # conn.execute(user1)
    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)
    chats_repo = database.repositories.ChatsRepo(context=context)
    # products_repo = database.repositories.ProductsRepo(context=context)
    # carts_repo = database.repositories.CartsRepo(context=context)
    # orders_repo = database.repositories.OrdersRepo(context=context)


# class MailSending:
#     sender = mail_sending.FileMailSender()


class Application:
    users = services.Users(user_repo=DB.users_repo)
    chats = services.Chats(chat_repo=DB.chats_repo)
    # checkout = services.Checkout(
    #     customers_repo=DB.customers_repo,
    #     products_repo=DB.products_repo,
    #     carts_repo=DB.carts_repo,
    #     orders_repo=DB.orders_repo,
    # )
    # orders = services.Orders(
    #     orders_repo=DB.orders_repo,
    #     mail_sender=MailSending.sender,
    # )
    # customers = services.Customers(customers_repo=DB.customers_repo)

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
    # checkout=Application.checkout,
    # orders=Application.orders,
    # customers=Application.customers,
)
