
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '552209705dd8e8bdbd1b8e2af324d5bb820832716d35a788833e9608322906299dc4934cbca8ef19b40c1fe2b4e86e6370a6'
    JWT_SECRET_KEY = 'ZDdkMmQxOGUxZjI2NzQxOTBjNGUyNmRiN2M1YTJmMmEyYTZiYTQyNjcxZGZkOTBmOWY1M2UyM2RjOTg3N2FiNGQxMmFjYjk4NGRhNmZlNTczOGQyOTkyMzcxYmJkZjQ3MjFkYjg1YTBiOTA4MDc1NmQ5OTA5ODFjMTE4MDFhMDg='
    JWT_ALGORITHM = 'HS512'

    # Database
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
    SECRET_KEY = '552209705dd8e8bdbd1b8e2af324d5bb820832716d35a788833e9608322906299dc4934cbca8ef19b40c1fe2b4e86e6370a6'
    JWT_SECRET_KEY = 'ZDdkMmQxOGUxZjI2NzQxOTBjNGUyNmRiN2M1YTJmMmEyYTZiYTQyNjcxZGZkOTBmOWY1M2UyM2RjOTg3N2FiNGQxMmFjYjk4NGRhNmZlNTczOGQyOTkyMzcxYmJkZjQ3MjFkYjg1YTBiOTA4MDc1NmQ5OTA5ODFjMTE4MDFhMDg='
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
