import reflex as rx

from app.components.navbar import navbar


@rx.page()
def index_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Hello world!"),
        rx.text("This is the index")
    )