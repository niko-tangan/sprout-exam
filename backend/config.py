from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API"
    admin_username: str = "admin"
    admin_password: str = "password"
    db_uri: str = "sqlite:///memory"

    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
