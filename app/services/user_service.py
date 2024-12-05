from app import User
from app.errors.authentication_errors import InvalidCredentialsError
from app.repositories.user_repository import UserRepository
from app.services.base_entity_service import BaseEntityService
from app.services.jwt_service import jwt_decode, jwt_encode
from app.services.password_service import verify_password
from app.states.storage import StorageState
from typing import Optional
from uuid import UUID


# Will contain business logic specific to the User entity
# This Service is class-based because it depends on stateful-operations (via the repositories) and benefits from inheritance
class UserService(BaseEntityService[UserRepository]):
    def get_session_user(self) -> Optional[User]:
        token = StorageState.jwt_token
        if not isinstance(token, str):
            return None

        uuid_string = jwt_decode(token)
        if not isinstance(uuid_string, str):
            return None

        try:
            uuid = UUID(uuid_string)
        except ValueError:
            return None

        user = self.repository.find_by_uuid(uuid)
        return user

    # Returns a new jwt token if the credentials are correct
    # ToDo: Email is subject to change, will depend on what the final login-identifier is
    def generate_session_token(self, email: str, password: str) -> str:
        user = self.repository.find_by_email(email)
        if not isinstance(user, User):
            raise InvalidCredentialsError

        if not verify_password(password, user.password_hash):
            raise InvalidCredentialsError

        return jwt_encode(user.get_uuid_string())

    def login(self, email: str, password: str) -> None:
        token = self.generate_session_token(email, password)
        StorageState.jwt_token = token