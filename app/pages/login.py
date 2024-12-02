import reflex as rx
from app import User
from app.services.password_service import hash_password
from app.state import user_repository, user_service, AppState
from app.styles.login import *
from typing import Optional


class DebugLoginState(rx.State):
    username: str
    password: str
    user: Optional[User]

    def create_user(self):
        password_hash = hash_password(self.password)

        user = User(
            first_name=self.username,
            last_name=self.username,
            email=self.username,
            password_hash=password_hash,
        )

        user_repository.save(user)

    def login(self):
        user_service.login(self.username, self.password)
        self.user = AppState.get_session_user()

def login_page():
    return rx.center(
            rx.container(
                rx.text("Login", **text_style),
                rx.input(
                    placeholder="Username",
                    on_change=DebugLoginState.set_username,
                    **input_style
                ),
                rx.input(
                    placeholder="Password",
                    type="password",
                    on_change=DebugLoginState.set_password,
                    **input_style,
                ),
                rx.button(
                    "Login",
                    on_click=DebugLoginState.login,
                    **button_style
                ),
                rx.button(
                    "DEBUG Register",
                    on_click=DebugLoginState.create_user,
                    **button_style
                ),
                rx.text(DebugLoginState.user.first_name, **text_style),
                **login_container_style
            ),
            **login_page_style
        )