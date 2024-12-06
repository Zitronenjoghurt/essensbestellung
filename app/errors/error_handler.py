from app.components.toasts import spawn_error_toast
from app.errors.app_error import AppUserError
from reflex.event import EventSpec
from typing import Optional


def custom_backend_error_handler(exception: Exception) -> Optional[EventSpec]:
    if isinstance(exception, AppUserError):
        return spawn_error_toast(exception.translate())
    else:
        raise exception