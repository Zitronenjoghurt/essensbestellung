import reflex as rx

from .constants.route import Route
from .pages.example import example_page
from .pages.index import index_page
from .styles.base import BASE_STYLE

# https://reflex.dev/docs/styling/theming/
THEME = rx.theme(
    appearance="dark",
    radius="large"
)

app = rx.App(style=BASE_STYLE)
app.add_page(index_page(), route=Route.ROOT)
app.add_page(example_page(), route=Route.EXAMPLE)