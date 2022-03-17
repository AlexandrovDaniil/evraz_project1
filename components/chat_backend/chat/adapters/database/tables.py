from datetime import datetime
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

# даем имя схемы только для БД MSSQL, связано с инфраструктурными особенностями
# metadata = MetaData(naming_convention=naming_convention, schema='app')

metadata = MetaData(naming_convention=naming_convention)

# yapf: disable

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('login', String, nullable=True),
    Column('password', String, nullable=True),
    Column('user_name', String, nullable=True),
)

chat = Table(
    'chat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_name', String, nullable=False),
    Column('description', String, nullable=False),
    Column('author_id', ForeignKey('user.id'), nullable=False),
    Column('create_time', String, nullable=False, default=str(datetime.now())),

)

chat_message = Table(
    'chat_message',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('chat_id', ForeignKey('chat.id'), nullable=False),
    Column('text', String, nullable=False),
    Column('send_time', String, nullable=False),
)

chat_members = Table(
    'chat_members',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('chat_id', ForeignKey('chat.id'), nullable=False),
    Column('alive', String, nullable=False),
    Column('banned', String, nullable=False),
)
