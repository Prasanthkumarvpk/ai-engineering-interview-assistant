from app.models.user import User

from app.repositories.user_repository import (
    UserRepository
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

class AuthService:

    def __init__(
        self,
        repo: UserRepository
    ):
        self.repo = repo

    def register(
        self,
        full_name,
        email,
        password
    ):

        existing = (
            self.repo.get_by_email(email)
        )

        if existing:
            raise Exception(
                "Email already exists"
            )

        user = User(
            full_name=full_name,
            email=email,
            password_hash=
            hash_password(password)
        )

        return self.repo.create(user)

    def login(
        self,
        email,
        password
    ):
        user = (
            self.repo.get_by_email(email)
        )

        if not user:
            raise Exception(
                "Invalid credentials"
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise Exception(
                "Invalid credentials"
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email
            }
        )

        return token
