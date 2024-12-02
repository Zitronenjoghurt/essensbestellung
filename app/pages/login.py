import reflex as rx
from rxconfig import config
from styles.login import (
    login_page_style, 
    login_container_style,
    text_style,
    input_style,
    button_style
)


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

app = rx.App()
app.add_page(login_page, route="/")