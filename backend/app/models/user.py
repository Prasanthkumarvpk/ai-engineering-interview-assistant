from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    full_name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    resumes = relationship(
        "Resume",
        back_populates="user"
    )

    interviews = relationship(
        "Interview",
        back_populates="user"
    )