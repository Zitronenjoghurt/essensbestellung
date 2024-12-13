import reflex as rx
from app import User
from app.constants.routes import Route
from app.errors.authentication_errors import InvalidSessionTokenError
from app.services.password_service import hash_password
from app.state import user_repository, user_service, AppState
from app.styles.login import *


class DebugLoginState(AppState):
    username: str
    password: str

    @rx.event
    def create_user(self):
        password_hash = hash_password(self.password)

        user = User(
            first_name=self.username,
            last_name=self.username,
            email=self.username,
            password_hash=password_hash,
        )

        user_repository.save(user)

        yield rx.toast(
            "User created!"
        )


    @rx.event
    def login(self):
        AppState.login(self.username, self.password)
        return rx.redirect(Route.LOGIN)

    @rx.event
    def check_logged_in(self):
        if self.is_authenticated():
            return rx.redirect(Route.ROOT)

@rx.page(route=Route.LOGIN, on_load=DebugLoginState.check_logged_in)
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
                **login_container_style
            ),
            **login_page_style
        )