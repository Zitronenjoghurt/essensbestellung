import reflex as rx

from app.components.navbar import navbar


# Reflex elements are functions which return some reflex component
# Pages are components which are accessible through routes and need to be passed to the app instance in app.py
@rx.page()
def index_page() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading("Hello world!"),
        rx.text("This is the index")
    )