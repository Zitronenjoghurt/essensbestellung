from pathlib import Path

APP_ROOT_PATH = Path(__file__).parent.parent
PROJECT_ROOT_PATH = APP_ROOT_PATH.parent

ENV_DEV_PATH = PROJECT_ROOT_PATH / '.env.dev'
ENV_PROD_PATH = PROJECT_ROOT_PATH / '.env.prod'
LOGS_PATH = PROJECT_ROOT_PATH / 'logs'

TRANSLATIONS_PATH = APP_ROOT_PATH / 'translations'