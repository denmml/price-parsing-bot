from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #основные настройки проекта
    PROJECT_NAME: str = "Price Monitoring Service"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"

    #настройки для базы данных и Redis
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    #Говорим пидантику, откуда брать перменные(.env)
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive=True,

    )


    settings = Settings()
