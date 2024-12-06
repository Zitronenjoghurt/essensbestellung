from app import User
from app.errors.authentication_errors import InvalidCredentialsError
from app.repositories.user_repository import UserRepository
from app.services.base_entity_service import BaseEntityService
from app.services.jwt_service import jwt_decode, jwt_encode
from app.services.password_service import verify_password
from app.states.storage import StorageState
from typing import Optional
from uuid import UUID


class UserService(BaseEntityService[UserRepository]):
    """
    Contains business logic specific to the User entity.
    This Service is class-based because it depends on stateful-operations (via the repositories) and benefits from inheritance.
    """

    def get_session_user(self) -> Optional[User]:
        """
        :return: The current session user or None, if there is no session token
        """

        token = StorageState.jwt_token
        if not isinstance(token, str):
            return None

        uuid_string = jwt_decode(token)
        uuid = UUID(uuid_string)

        user = self.repository.find_by_uuid(uuid)
        return user

    def generate_session_token(self, email: str, password: str) -> str:
        """
        Generates a new session token for the given user credentials.
        :param email: The users email
        :param password: The users password
        :return: valid JWT token
        """

        user = self.repository.find_by_email(email)
        if not isinstance(user, User):
            raise InvalidCredentialsError

        if not verify_password(password, user.password_hash):
            raise InvalidCredentialsError

        return jwt_encode(user.get_uuid_string())
