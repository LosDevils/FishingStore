from dataclasses import dataclass

from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseConfig(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


@dataclass()
class Config:
    database: DataBaseConfig


config = Config(database=DataBaseConfig())
