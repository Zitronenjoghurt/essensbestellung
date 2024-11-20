import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_DEV_PATH = os.path.join(PROJECT_ROOT_PATH, '.env.dev')
ENV_PROD_PATH = os.path.join(PROJECT_ROOT_PATH, '.env.prod')