from typing import Optional

import reflex as rx

from app import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


# Central access to repositories and class-based services
# they don't need to be newly instantiated with every use
user_repository: UserRepository = UserRepository()

user_service: UserService = UserService(user_repository)

# The app state will hold all kinds of information about a user's session
# E.g. the session user entity from the database and other session-specific data
class AppState(rx.State):
    session_user: Optional[User] = None
    is_loading: bool = False