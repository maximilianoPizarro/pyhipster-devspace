
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '567ed61f9f9fa26334e883ef4da82024388f7fb54dbfd0c0ad5b0a482d1c0b9ab7201a9e43032e60738cd74e8c674ce39534'
    JWT_SECRET_KEY = 'ZjIzMGMzYjZjNWRjMjlkMWYzYTM5MWJhOTBlZjEzN2FmNGIzNmEyMDllZDQzYWRhODQxNGQxMTY1YzBkNGQ1ZmUxZTQ0OTYyNWE5NDY2YTUyMDZiYmRhNzgzMjJhMmRlM2ZhMjNmOTRmMThmZWY1NGZlYmYyOWM2MzE5ODc4Nzk='
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
    SECRET_KEY = '567ed61f9f9fa26334e883ef4da82024388f7fb54dbfd0c0ad5b0a482d1c0b9ab7201a9e43032e60738cd74e8c674ce39534'
    JWT_SECRET_KEY = 'ZjIzMGMzYjZjNWRjMjlkMWYzYTM5MWJhOTBlZjEzN2FmNGIzNmEyMDllZDQzYWRhODQxNGQxMTY1YzBkNGQ1ZmUxZTQ0OTYyNWE5NDY2YTUyMDZiYmRhNzgzMjJhMmRlM2ZhMjNmOTRmMThmZWY1NGZlYmYyOWM2MzE5ODc4Nzk='
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
