import os

import reflex as rx
from dotenv import load_dotenv

from . import Role, User
from .constants.paths import ENV_DEV_PATH
from .constants.permissions import Permission
from .constants.routes import Route
from .pages.example import example_page
from .pages.index import index_page
from .state import role_repository, user_repository
from .styles.base import BASE_STYLE


# https://reflex.dev/docs/styling/theming/
THEME = rx.theme(
    appearance="dark",
    radius="large"
)

# Builds the app and registers all routes
app = rx.App(style=BASE_STYLE)
app.add_page(index_page(), route=Route.ROOT)
app.add_page(example_page(), route=Route.EXAMPLE)

# Loads the development env file as fallback if no env file was loaded
# e.g. if the app was started outside the docker container
dev_mode = os.environ.get('DEV_MODE')
if dev_mode is None:
    load_dotenv(ENV_DEV_PATH)


# Initial test code to confirm proof-of-concept, WORKS!
# Won't work if initial migrations did not run yet
#new_role = Role(name='test', permissions=[Permission.RECEIVE_MEALS])
#new_user = User(
#    first_name='John',
#    last_name='Doe',
#    email='<EMAIL>',
#    password_hash='<PASSWORD>',
#)
#
#role_repository.save(new_role)
#
#new_user.roles.append(new_role)
#user_repository.save(new_user)
#
#john_doe = user_repository.find_one_by(first_name='John', last_name='Doe')
#assert john_doe is not None
#assert len(john_doe.roles) == 1
#assert john_doe.roles[0].name == new_role.name