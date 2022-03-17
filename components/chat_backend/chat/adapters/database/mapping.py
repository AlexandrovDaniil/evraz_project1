from sqlalchemy.orm import registry, relationship

from chat.application import dataclasses

from . import tables

mapper = registry()

mapper.map_imperatively(dataclasses.User, tables.user)

mapper.map_imperatively(
    dataclasses.Chat,
    tables.chat,
    properties={
        'members_list': relationship(
            dataclasses.ChatMembers,
            lazy='subquery'
        ),
        'message_list': relationship(
            dataclasses.ChatMessage,
            lazy='subquery'
        )
    }
)

mapper.map_imperatively(dataclasses.ChatMembers, tables.chat_members)
mapper.map_imperatively(dataclasses.ChatMessage, tables.chat_message)

