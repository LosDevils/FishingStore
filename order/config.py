from dataclasses import dataclass

from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_DRIVER: str

    model_config = SettingsConfigDict(env_file=".env", encoding="utf-8", env_prefix="database")


@dataclass
class ProjectConfig(BaseSettings):
    database: DataBaseConfig


config = ProjectConfig(database=DataBaseConfig())
