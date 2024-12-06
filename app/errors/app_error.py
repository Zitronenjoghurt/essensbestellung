from app.services.i18n_service import translate
from app.translations.keys import i18nKey


class AppUserError(Exception):
    """
    Base class for exceptions of this application which are supposed to be propagated to the user.
    """
    TRANSLATION_KEY: i18nKey = i18nKey.ERROR_APP

    def translate(self, **kwargs) -> str:
        return translate(self.TRANSLATION_KEY, **kwargs)