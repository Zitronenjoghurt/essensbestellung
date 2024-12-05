from enum import Enum


# All new keys added in de.yml and en.yml have to be added here too
# This will ensure consistent key naming and prevent using non-existent keys
# You can use the translate() function from the i18n service to translate the keys to the currently set locale
class i18nKey(str, Enum):
    GENERAL_ERROR = "general.error"

    HOME_WELCOME = "home.welcome"

    PERMISSION_RECEIVE_MEALS = "permission.receive_meals"
    PERMISSION_SERVICE_MEALS = "permission.service_meals"

    ERROR_APP = "error.app"
    ERROR_AUTHENTICATION = "error.authentication"
    ERROR_EXPIRED_SESSION_TOKEN = "error.expired_session_token"
    ERROR_INVALID_CREDENTIALS = "error.invalid_credentials"
    ERROR_INVALID_SESSION_TOKEN = "error.invalid_session_token"