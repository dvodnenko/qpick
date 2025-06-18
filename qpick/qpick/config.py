import os

from dotenv import load_dotenv


load_dotenv(override=True)

SECRET_APP_KEY = os.getenv('secret_app_key')
