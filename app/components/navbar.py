import reflex as rx
from app.constants.routes import Route


# CSS styles can be passed as a style instance to reflex components
# https://reflex.dev/docs/styling/common-props/
STYLE = rx.Style()

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link("Home", href=Route.ROOT),
            rx.link("Example", href=Route.EXAMPLE),
        ),
        style=STYLE,
    )