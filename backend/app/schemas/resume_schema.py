from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    file_name: str
    status: str

    class Config:
        from_attributes = True