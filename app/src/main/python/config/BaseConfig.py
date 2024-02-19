
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '1573221ffca496fd8a97fd8012a784af24733ba0fcb94d0d48a6a996392d2a3bd9aea315ac3212f224dab24c69c4c4f6c799'
    JWT_SECRET_KEY = 'ZDMwZTA1MmQ4YjIyMGY5Y2EzNWVjZTY4YjIzMjAwMmMxNmEyZGM2NmYwYTMwMmY1NjY0YTcwZmUwZDEyYzk4Zjk4Yjg1YmY1MTg4OTk3NTc0ODczNDU2NDAxMzNhYWY3OTczZDNmMDE4NDQ0YzcxNzllOTE3NTNmZmFhZDRlODE='
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
    SECRET_KEY = '1573221ffca496fd8a97fd8012a784af24733ba0fcb94d0d48a6a996392d2a3bd9aea315ac3212f224dab24c69c4c4f6c799'
    JWT_SECRET_KEY = 'ZDMwZTA1MmQ4YjIyMGY5Y2EzNWVjZTY4YjIzMjAwMmMxNmEyZGM2NmYwYTMwMmY1NjY0YTcwZmUwZDEyYzk4Zjk4Yjg1YmY1MTg4OTk3NTc0ODczNDU2NDAxMzNhYWY3OTczZDNmMDE4NDQ0YzcxNzllOTE3NTNmZmFhZDRlODE='
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
