from app.services.i18n_service import translate
from app.translations.keys import i18nKey


class AppError(Exception):
    """
    Base class for exceptions of this application.
    """
    TRANSLATION_KEY: i18nKey = i18nKey.ERROR_APP

    def translate(self, **kwargs) -> str:
        return translate(self.TRANSLATION_KEY, **kwargs)