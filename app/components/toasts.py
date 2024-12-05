import reflex as rx
from reflex.event import EventSpec

from app.services.i18n_service import translate
from app.translations.keys import i18nKey


def spawn_error_toast(error: str) -> EventSpec:
    return rx.toast.error(
        title=translate(i18nKey.GENERAL_ERROR),
        description=error,
        position="top-center",
        close_button=True,
        important=True,
        duration=20 * 1000,
    )