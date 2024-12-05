import reflex as rx
import os
from dotenv import load_dotenv
from .constants.paths import ENV_DEV_PATH
from .errors.error_handler import custom_backend_error_handler
from .styles.base import BASE_STYLE

# https://reflex.dev/docs/styling/theming/
THEME = rx.theme(
    appearance="dark",
    radius="large"
)

# Builds the app and registers all routes
app = rx.App(
    style=BASE_STYLE,
    theme=THEME,
    backend_exception_handler=custom_backend_error_handler
)

# Loads the development env file as fallback if no env file was loaded
# e.g. if the app was started outside the docker container
dev_mode = os.environ.get('DEV_MODE')
if dev_mode is None:
    load_dotenv(ENV_DEV_PATH)
