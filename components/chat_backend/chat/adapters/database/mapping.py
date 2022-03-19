from chat.application import dataclasses
from sqlalchemy.orm import registry, relationship

from . import tables

mapper = registry()

mapper.map_imperatively(dataclasses.User, tables.user)
mapper.map_imperatively(dataclasses.Chat, tables.chat)


mapper.map_imperatively(dataclasses.ChatMembers, tables.chat_members)
mapper.map_imperatively(dataclasses.ChatMessage, tables.chat_message)
