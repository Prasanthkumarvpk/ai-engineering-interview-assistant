import os

from app.models.resume import Resume

from app.utils.pdf_parser import (
    extract_pdf_text
)


class ResumeService:

    def __init__(
        self,
        repo
    ):
        self.repo = repo

    def create_resume(
        self,
        user_id,
        file_name,
        file_path,
        file_size
    ):

        resume = Resume(
            user_id=user_id,
            file_name=file_name,
            file_path=file_path,
            file_size=file_size,
            status="UPLOADED"
        )

        return self.repo.create(
            resume
        )

    def process_resume(
        self,
        resume
    ):

        resume.status = "PROCESSING"

        self.repo.update(
            resume
        )

        try:
            text = extract_pdf_text(
                resume.file_path
            )
        except Exception:
            resume.status = "FAILED"

            self.repo.update(
                resume
            )

            raise

        resume.extracted_text = text

        resume.status = "COMPLETED"

        return self.repo.update(
            resume
        )
