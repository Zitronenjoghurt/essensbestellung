import reflex as rx
import os

DB_URL = os.environ.get('DATABASE_URL')
if not DB_URL:
    raise RuntimeError("DATABASE_URL env variable not set, make sure you're running this within the docker container")

config = rx.Config(
    app_name="app",
    db_url=DB_URL,
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)