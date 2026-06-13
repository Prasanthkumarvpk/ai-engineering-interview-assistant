from jose import jwt
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=["HS256"]
        )

        return payload

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )