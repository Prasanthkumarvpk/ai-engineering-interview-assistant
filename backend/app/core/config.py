from urllib.parse import quote
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = "AI Interview Assistant"
    APP_VERSION: str = "1.0.0"

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    JWT_SECRET: str
    OPENAI_API_KEY: str
    REDIS_URL: str

    @property
    def DATABASE_URL(self):
        # Safely encode password to handle special characters
        encoded_password = quote(self.MYSQL_PASSWORD, safe='')
        return f"mysql+pymysql://{self.MYSQL_USER}:{encoded_password}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"


settings = Settings()
