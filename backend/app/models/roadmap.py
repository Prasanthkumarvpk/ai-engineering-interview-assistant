from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.models.base_model import BaseModel


class Roadmap(BaseModel):
    __tablename__ = "roadmaps"

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    roadmap_text = Column(
        Text
    )
