# from app.db.session import SessionLocal


# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()

from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()