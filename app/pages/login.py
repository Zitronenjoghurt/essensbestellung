import reflex as rx
from app.styles.login import *


def login_page():
    return rx.center(
            rx.container(
                rx.text("Login", **text_style),
                rx.input(placeholder="Username", **input_style),
                rx.input(placeholder="Password", type="password",**input_style),
                rx.button("Login", **button_style),
                **login_container_style
            ),
            **login_page_style
        )