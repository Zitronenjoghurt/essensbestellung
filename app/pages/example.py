import reflex as rx

from app.components.navbar import navbar
from app.constants.routes import Route
from app.pages.login import DebugLoginState
from app.state import AppState


@rx.page(route=Route.EXAMPLE, on_load=DebugLoginState.check_logged_in)
def example_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Hello example or something"),
        rx.text("This is an example page")
    )