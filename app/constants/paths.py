import os

APP_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT_PATH = os.path.dirname(APP_ROOT_PATH)

ENV_DEV_PATH = os.path.join(PROJECT_ROOT_PATH, '.env.dev')
ENV_PROD_PATH = os.path.join(PROJECT_ROOT_PATH, '.env.prod')

TRANSLATIONS_PATH = os.path.join(APP_ROOT_PATH, 'translations')