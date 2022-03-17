from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = 'sqlite:////tmp/chat.db'

