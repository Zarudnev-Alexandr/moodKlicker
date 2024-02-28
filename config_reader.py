import os

from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, SecretStr

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    bot_token: SecretStr = os.getenv("bot_token")
    db_url: PostgresDsn = os.getenv("db_url")

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Settings()
