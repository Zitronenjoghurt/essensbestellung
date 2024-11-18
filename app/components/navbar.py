import reflex as rx

from app.constants.route import Route

STYLE = rx.Style(
    background="whiteAlpha.500"
)

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link("Home", href=Route.ROOT),
            rx.link("Example", href=Route.EXAMPLE),
        ),
        style=STYLE,
    )