import reflex as rx
from app.services.jwt_service import JWT_EXPIRY_MINUTES
from typing import Optional


class StorageState(rx.State):
    jwt_token: Optional[str] = rx.Cookie(
        name='jwt_token',
        secure=True,
        max_age=JWT_EXPIRY_MINUTES * 60
    )