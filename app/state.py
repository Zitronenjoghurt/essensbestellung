import reflex as rx
from reflex.event import EventSpec

from app import User
from app.constants.routes import Route
from app.errors.authentication_errors import InvalidCredentialsError
from app.logger import LOGGER
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.services.role_service import RoleService
from app.services.user_service import UserService
from typing import Optional
from app.states.storage import StorageState


# Central access to repositories and class-based services
# they don't need to be newly instantiated with every use
role_repository: RoleRepository = RoleRepository()
user_repository: UserRepository = UserRepository()
role_service: RoleService = RoleService(role_repository)
user_service: UserService = UserService(user_repository)

# The app state will hold all kinds of information about a user's session
# E.g. the session user entity from the database and other session-specific data
class AppState(rx.State):
    session_user: Optional[User] = None
    is_loading: bool = False

    def fetch_session_user(self) -> Optional[User]:
        if not isinstance(self.session_user, User):
            self.session_user = user_service.get_session_user()
        return self.session_user

    def is_authenticated(self):
        user = self.fetch_session_user()
        return isinstance(user, User) and StorageState.jwt_token is not None

    @rx.event
    def check_auth(self):
        if not self.is_authenticated():
            return rx.redirect(Route.LOGIN)
        
    @staticmethod
    def login(email: str, password: str) -> None:
        """
        If the credentials are correct, the user will be logged in by storing a new session token in a cookie.
        :param email: The users email
        :param password: The users password
        """
        token = user_service.generate_session_token(email, password)
        StorageState.jwt_token = token

    def logout(self) -> EventSpec:
        self.session_user = None
        StorageState.clear_jwt_token()
        return rx.redirect(Route.LOGIN)