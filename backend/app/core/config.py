from pydantic_settings import BaseSettings


class Settings(BaseSettings):
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

    class Config:
        env_file = ".env"


settings = Settings()