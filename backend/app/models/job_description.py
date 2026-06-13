from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class JobDescription(BaseModel):
    __tablename__ = "job_descriptions"

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    title = Column(
        String(255)
    )

    company = Column(
        String(255)
    )

    description = Column(
        Text
    )
