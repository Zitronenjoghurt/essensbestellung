from typing import Optional

import reflex as rx


class AuthState(rx.State):
    jwt_token: Optional[str] = rx.LocalStorage()