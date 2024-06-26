import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_DRIVER: str

    model_config = SettingsConfigDict(env_file=".env", )


class ProjectConfig(BaseSettings):
    database: DataBaseConfig
