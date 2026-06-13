from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Interview(BaseModel):
    __tablename__ = "interviews"

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    status = Column(
        String(50)
    )

    score = Column(
        Integer,
        default=0
    )

    user = relationship(
        "User",
        back_populates="interviews"
    )

    questions = relationship(
        "Question",
        back_populates="interview"
    )