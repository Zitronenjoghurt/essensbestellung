import os

import reflex as rx
from dotenv import load_dotenv

from .constants.paths import ENV_DEV_PATH
from .constants.routes import Route
from .pages.example import example_page
from .pages.index import index_page
from .styles.base import BASE_STYLE


# https://reflex.dev/docs/styling/theming/
THEME = rx.theme(
    appearance="dark",
    radius="large"
)

# Builds the app and registers all routes
app = rx.App(style=BASE_STYLE, theme=THEME)
app.add_page(index_page(), route=Route.ROOT)
app.add_page(example_page(), route=Route.EXAMPLE)

# Loads the development env file as fallback if no env file was loaded
# e.g. if the app was started outside the docker container
dev_mode = os.environ.get('DEV_MODE')
if dev_mode is None:
    load_dotenv(ENV_DEV_PATH)
