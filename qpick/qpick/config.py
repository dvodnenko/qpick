import os

from dotenv import load_dotenv


load_dotenv(override=True)


## app ##

SECRET_APP_KEY = os.getenv('secret_app_key')

## database ##

DATABASE_NAME = os.getenv('database_name')
DATABASE_USER = os.getenv('database_user')
DATABASE_PASSWORD = os.getenv('database_password')
DATABASE_HOST = os.getenv('database_host')
DATABASE_PORT = int(os.getenv('database_port'))
