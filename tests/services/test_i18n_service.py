from app.constants.locales import Locale
from app.constants.permissions import Permission
from app.services.i18n_service import translate_permission, set_locale, translate
from app.translations.keys import i18nKey


def test_translate():
    set_locale(Locale.GERMAN)
    welcome_de = translate(i18nKey.HOME_WELCOME)
    set_locale(Locale.ENGLISH)
    welcome_en = translate(i18nKey.HOME_WELCOME)

    assert welcome_de == "Willkommen"
    assert welcome_en == "Welcome"

def test_translate_permission():
    set_locale(Locale.GERMAN)
    receive_meals_de = translate_permission(Permission.RECEIVE_MEALS)
    set_locale(Locale.ENGLISH)
    receive_meals_en = translate_permission(Permission.RECEIVE_MEALS)

    assert receive_meals_de == "Mahlzeiten erhalten"
    assert receive_meals_en == "Receive meals"