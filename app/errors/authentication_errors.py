from app.errors.app_error import AppError
from app.translations.keys import i18nKey


class AuthenticationError(AppError):
    TRANSLATION_KEY = i18nKey.ERROR_AUTHENTICATION

class ExpiredSessionTokenError(AuthenticationError):
    TRANSLATION_KEY = i18nKey.ERROR_EXPIRED_SESSION_TOKEN

class InvalidSessionTokenError(AuthenticationError):
    TRANSLATION_KEY = i18nKey.ERROR_INVALID_SESSION_TOKEN

class InvalidCredentialsError(AuthenticationError):
    TRANSLATION_KEY = i18nKey.ERROR_INVALID_CREDENTIALS