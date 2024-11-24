from enum import Enum


# All new keys added in de.yml and en.yml have to be added here too
# This will ensure consistent key naming and prevent using non-existent keys
# You can use the translate() function from the i18n service to translate the keys to the currently set locale
class i18nKey(str, Enum):
    HOME_WELCOME = "home.welcome"

    PERMISSION_RECEIVE_MEALS = "permission.receive_meals"