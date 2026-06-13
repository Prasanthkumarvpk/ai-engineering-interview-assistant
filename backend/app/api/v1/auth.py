from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from google.oauth2 import id_token
from google.auth.transport import requests

from sqlalchemy.orm import Session

from app.database_dependency import get_db

from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

from app.services.auth_service import (
    AuthService
)

from app.repositories.user_repository import (
    UserRepository
)


from app.dependencies.auth_dependency import (
    get_current_user
)

from app.schemas.auth_schema import GoogleAuthRequest

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    repo = UserRepository(db)

    service = AuthService(repo)

    try:
        user = service.register(
            request.full_name,
            request.email,
            request.password
        )
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    return {
        "message": "User created",
        "user_id": user.id
    }

@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    repo = UserRepository(db)

    service = AuthService(repo)

    try:
        token = service.login(
            request.email,
            request.password
        )
    except Exception as exc:
        raise HTTPException(
            status_code=401,
            detail=str(exc)
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }   

@router.get("/me")
def me(
    current_user=Depends(
        get_current_user
    )
):
    return current_user

@router.post("/google")
def google_login(request: GoogleAuthRequest, db: Session = Depends(get_db)):
    try:
        id_info = id_token.verify_oauth2_token(
            request.credential,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )

        email = id_info["email"]
        full_name = id_info.get("name", "")

        repo = UserRepository(db)
        service = AuthService(repo)

        token = service.login_or_create_google_user(email, full_name)

        return {"access_token": token, "token_type": "bearer"}

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
