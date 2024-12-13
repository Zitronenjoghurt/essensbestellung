import traceback

from app.components.toasts import spawn_error_toast
from app.errors.app_error import AppUserError
from reflex.event import EventSpec
from typing import Optional

from app.logger import LOGGER


def custom_error_handler(exception: Exception) -> Optional[EventSpec]:
    if isinstance(exception, AppUserError):
        return spawn_error_toast(exception.translate())
    else:
        stringified_exception = stringify_exception(exception)
        LOGGER.error(stringified_exception)
        raise exception

def stringify_exception(exception: Exception) -> str:
    tb = traceback.extract_tb(exception.__traceback__)
    error_msg = f"{type(exception).__name__}: {str(exception)}"

    attrs = []
    for attr in ['code', 'reason', 'details', 'hint']:
        if hasattr(exception, attr):
            value = getattr(exception, attr)
            if value:
                attrs.append(f"{attr}: {value}")

    if attrs:
        error_msg += "\n" + "\n".join(attrs)

    if tb:
        last_frame = tb[-1]
        error_msg += f"\nLocation: {last_frame.filename}:{last_frame.lineno} in {last_frame.name}"

    return error_msg