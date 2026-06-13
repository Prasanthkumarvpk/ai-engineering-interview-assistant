from fastapi import FastAPI

from app.api.v1.router import api_router
from app.middleware.error_handler import (
    global_exception_handler
)

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app import models


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(
        bind=engine
    )


@app.get("/")
def root():
    return {
        "message": "AI Interview Assistant API"
    }
