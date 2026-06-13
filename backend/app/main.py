# # from fastapi import FastAPI

# # from app.api.v1.router import api_router
# # from app.middleware.error_handler import (
# #     global_exception_handler
# # )

# # from app.core.config import settings
# # from app.db.base import Base
# # from app.db.database import engine
# # from app import models


# # app = FastAPI(
# #     title=settings.APP_NAME,
# #     version=settings.APP_VERSION
# # )

# # app.include_router(
# #     api_router,
# #     prefix="/api/v1"
# # )

# # app.add_exception_handler(
# #     Exception,
# #     global_exception_handler
# # )


# # @app.on_event("startup")
# # def startup():
# #     Base.metadata.create_all(
# #         bind=engine
# #     )


# # @app.get("/")
# # def root():
# #     return {
# #         "message": "AI Interview Assistant API"
# #     }


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.v1.router import api_router
# from app.middleware.error_handler import global_exception_handler
# from app.core.config import settings
# from app.db.base import Base
# from app.db.database import engine
# from app import models

# app = FastAPI(
#     title=settings.APP_NAME,
#     version=settings.APP_VERSION
# )

# # =========================
# # CORS FIX (IMPORTANT)
# # =========================
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",  # React Vite frontend
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # =========================
# # ROUTES
# # =========================
# app.include_router(
#     api_router,
#     prefix="/api/v1"
# )

# # =========================
# # EXCEPTION HANDLER
# # =========================
# app.add_exception_handler(
#     Exception,
#     global_exception_handler
# )

# # =========================
# # STARTUP
# # =========================
# @app.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)

# # =========================
# # ROOT
# # =========================
# @app.get("/")
# def root():
#     return {
#         "message": "AI Interview Assistant API"
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.middleware.error_handler import global_exception_handler
from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app import models

# =========================
# APP INIT
# =========================
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# =========================
# CORS (FIXED + SAFE CONFIG)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTES
# =========================
app.include_router(
    api_router,
    prefix="/api/v1"
)

# =========================
# GLOBAL ERROR HANDLER
# =========================
app.add_exception_handler(
    Exception,
    global_exception_handler
)

# =========================
# STARTUP EVENT
# =========================
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AI Interview Assistant API"
    }

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {
        "message": "AI Interview Assistant API is running"
    }