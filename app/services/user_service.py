from typing import Optional

from uuid import UUID

from app import User
from app.repositories.user_repository import UserRepository
from app.services.base_entity_service import BaseEntityService
from app.services.jwt_service import jwt_decode, jwt_encode
from app.services.password_service import verify_password
from app.states.storage import StorageState


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
    # ToDo: Throw different errors depending on what went from
    def login(self, email: str, password: str) -> Optional[str]:
        user = self.repository.find_by_email(email)
        if not isinstance(user, User):
            return None

        if not verify_password(password, user.password_hash):
            return None

        return jwt_encode(user.uuid_string)