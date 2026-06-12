from sqlalchemy import create_engine
from app.core.config import settings

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.MYSQL_USER}:"
    f"{settings.MYSQL_PASSWORD}@"
    f"{settings.MYSQL_HOST}:"
    f"{settings.MYSQL_PORT}/"
    f"{settings.MYSQL_DB}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)