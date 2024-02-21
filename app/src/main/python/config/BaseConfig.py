
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '9977c09fe81686da33f66b281c6e6afce72cef60bd8d5665cfbffea3ea944d8536ef8567a1a5bcb4340bcc4f72a20dca56c7'
    JWT_SECRET_KEY = 'MTJhY2E0YjNjYmNjYzczMmE0MjY2MTU1ZGUyZWMxZjA5NDliM2Q3YzU4YWRkMDU0ZmRkMWY0MmZhOGQ0OWJhZGVkMjFmYjJiZDA1Zjk1MTAxZWY3YmVmMGIyODdmYTBlN2JlYjViYjc3NWE4MzYyZGI1ZjIxNjU2NGM1MWU0Y2U='
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
    SECRET_KEY = '9977c09fe81686da33f66b281c6e6afce72cef60bd8d5665cfbffea3ea944d8536ef8567a1a5bcb4340bcc4f72a20dca56c7'
    JWT_SECRET_KEY = 'MTJhY2E0YjNjYmNjYzczMmE0MjY2MTU1ZGUyZWMxZjA5NDliM2Q3YzU4YWRkMDU0ZmRkMWY0MmZhOGQ0OWJhZGVkMjFmYjJiZDA1Zjk1MTAxZWY3YmVmMGIyODdmYTBlN2JlYjViYjc3NWE4MzYyZGI1ZjIxNjU2NGM1MWU0Y2U='
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
