
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = 'a0e9fe4dbbd795a94cbf1b292743a8924f7e1616b6e1ea3914cf1b06c96564177737dc5ee7181e12a250b12873c2ccb65eee'
    JWT_SECRET_KEY = 'NTliZTYzZjU3NGFhZDQ5MjRlOTUxYzQzMDI2NGU1YTM3ZTJlMjQ0Njc3NTRiNDJkMDdmOTkxZThlZjMxNzI0ZWJiZTY3ZjdkMGNhN2QyNDU2MjAzOTQwOWVmYWU3M2Q3OGVjMGY5N2RiMDZiNWU4ZDhjMmFlNzQ3MzAyYWYxM2E='
    JWT_ALGORITHM = 'HS512'

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<user>:<password>@<host>[:<port>]/<dbname>[?key=value&key=value...]'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = False
    SQLALCHEMY_EXPIRE_ON_COMMIT = False

    # Mail Configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'my-email-id@gmail.com'
    MAIL_PASSWORD = 'my-email-password'

    # Cache Configurations
    
class ProdConfig:
    # Flask 
    ENV = 'production'
    FLASK_ENV = 'production'
    SECRET_KEY = 'a0e9fe4dbbd795a94cbf1b292743a8924f7e1616b6e1ea3914cf1b06c96564177737dc5ee7181e12a250b12873c2ccb65eee'
    JWT_SECRET_KEY = 'NTliZTYzZjU3NGFhZDQ5MjRlOTUxYzQzMDI2NGU1YTM3ZTJlMjQ0Njc3NTRiNDJkMDdmOTkxZThlZjMxNzI0ZWJiZTY3ZjdkMGNhN2QyNDU2MjAzOTQwOWVmYWU3M2Q3OGVjMGY5N2RiMDZiNWU4ZDhjMmFlNzQ3MzAyYWYxM2E='
    JWT_ALGORITHM = 'HS512'

    # Database
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = False
    SQLALCHEMY_EXPIRE_ON_COMMIT = False

    # Mail Configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'my-email-id@gmail.com'
    MAIL_PASSWORD = 'my-email-password'

    # Cache Configurations
