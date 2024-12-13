import reflex as rx
from app.components.navbar import navbar
from app.constants.routes import Route
from app.pages.login import DebugLoginState
from app.state import AppState


class IndexState(AppState):
    @rx.var
    def full_name(self) -> str:
        if self.session_user is None:
            return "undefined"
        return self.session_user.get_full_name()

# Reflex elements are functions which return some reflex component
# Pages are components which are accessible through routes and need to be passed to the app instance in app.py
@rx.page(route=Route.ROOT, on_load=AppState.check_auth)
def index_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Hello world!"),
        rx.cond(
            AppState.session_user is not None,
            rx.vstack(
                rx.heading(f"Welcome {IndexState.full_name}"),
                rx.text(f"Email: {AppState.session_user.email}"),
                rx.button(
                    "Logout",
                    on_click=AppState.logout,
                ),
            ),
        )
    )

