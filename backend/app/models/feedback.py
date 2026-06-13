from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.models.base_model import BaseModel


class Feedback(BaseModel):
    __tablename__ = "feedbacks"

    interview_id = Column(
        Integer,
        ForeignKey("interviews.id")
    )

    strengths = Column(
        Text
    )

    weaknesses = Column(
        Text
    )

    recommendations = Column(
        Text
    )
