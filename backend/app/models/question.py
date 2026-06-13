from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Question(BaseModel):
    __tablename__ = "questions"

    interview_id = Column(
        Integer,
        ForeignKey("interviews.id")
    )

    question_text = Column(
        String(5000)
    )

    difficulty = Column(
        String(50)
    )

    interview = relationship(
        "Interview",
        back_populates="questions"
    )