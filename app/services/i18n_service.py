from typing import Optional

import i18n
from app.constants.locales import Locale
from app.constants.paths import TRANSLATIONS_PATH
from app.constants.permissions import Permission
from app.translations.keys import i18nKey


i18n.set('locale', Locale.GERMAN.value)
i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append(TRANSLATIONS_PATH)
i18n.set('fallback_language', Locale.ENGLISH.value)

def set_locale(locale: Locale) -> None:
    i18n.set('locale', locale.value)

def translate(key: i18nKey, locale: Optional[Locale] = None, **kwargs) -> str:
    if isinstance(locale, Locale):
        return i18n.t(key.value, locale=locale.value, **kwargs)
    else:
        return i18n.t(key.value, **kwargs)

def translate_permission(permission: Permission) -> str:
    key = f"permission.{permission.value.lower()}"
    result = i18n.t(key)
    return result