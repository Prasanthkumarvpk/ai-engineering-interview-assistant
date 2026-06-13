import os
import uuid
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database_dependency import get_db

from app.repositories.resume_repository import (
    ResumeRepository
)

from app.services.resume_service import (
    ResumeService
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads/resumes"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="PDF only"
        )

    file_id = str(
        uuid.uuid4()
    )

    path = (
        f"{UPLOAD_DIR}/"
        f"{file_id}.pdf"
    )

    with open(
        path,
        "wb"
    ) as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    file_size = os.path.getsize(
        path
    )

    repo = ResumeRepository(db)

    service = ResumeService(
        repo
    )

    resume = service.create_resume(
        user_id=1,
        file_name=file.filename,
        file_path=path,
        file_size=file_size
    )

    try:
        service.process_resume(
            resume
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file"
        )

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "file_name": file.filename
    }
