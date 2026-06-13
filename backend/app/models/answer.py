from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.models.base_model import BaseModel


class Answer(BaseModel):
    __tablename__ = "answers"

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    answer_text = Column(
        String(10000)
    )

    score = Column(
        Integer
    )