from typing import Optional

import reflex as rx

from app import User
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.services.role_service import RoleService
from app.services.user_service import UserService


# Central access to repositories and class-based services
# they don't need to be newly instantiated with every use
role_repository: RoleRepository = RoleRepository()
user_repository: UserRepository = UserRepository()
role_service: RoleService = RoleService(role_repository)
user_service: UserService = UserService(user_repository)

# The app state will hold all kinds of information about a user's session
# E.g. the session user entity from the database and other session-specific data
class AppState(rx.State):
    _session_user: Optional[User] = None
    is_loading: bool = False

    @classmethod
    def get_session_user(cls) -> Optional[User]:
        if not isinstance(cls._session_user, User):
            cls._session_user = user_service.get_session_user()
        return cls._session_user