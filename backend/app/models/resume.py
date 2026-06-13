from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Resume(BaseModel):
    __tablename__ = "resumes"

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    file_name = Column(
        String(500),
        nullable=False
    )

    file_path = Column(
        String(1000),
        nullable=False
    )

    file_size = Column(
        Integer
    )

    status = Column(
        String(50),
        default="UPLOADED"
    )

    extracted_text = Column(
        Text
    )

    user = relationship(
        "User",
        back_populates="resumes"
    )