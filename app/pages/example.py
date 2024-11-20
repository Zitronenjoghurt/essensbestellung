import reflex as rx

from app.components.navbar import navbar


@rx.page()
def example_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Hello example or something"),
        rx.text("This is an example page")
    )