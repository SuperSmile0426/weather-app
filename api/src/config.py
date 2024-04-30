from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DATABASE_USER: str = Field("", env="DATABASE_USER")
    DATABASE_PASSWORD: str = Field("", env="DATABASE_PASSWORD")
    DATABASE_DB: str = Field("", env="DATABASE_DB")

    class Config:
        env_prefix = ""
        # case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}
