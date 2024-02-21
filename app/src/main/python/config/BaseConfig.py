
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '0d0ad7e44b96ba60565ed72fd00313bd5539879bde7385d41c6935ab34ee12b3b59e8486059bd9b0fc8d58ba3b0b293fefde'
    JWT_SECRET_KEY = 'ZWNjMDJjN2E0ZmU1MTJlZDZlNTI1M2E2NTA3NDJhZWYwMDYzNjk2N2RjMDczNjQ1OWRhZDcxNjM0MWYxNzI5OWRkYjE4NDIxYzQ0MzY1YTBhZTQ2Y2NhNjRjYTVmNWZhYWEyYjVkYzRmMjIwYTExZGRlYTA0NzA4ZWQyODdhMDk='
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
    SECRET_KEY = '0d0ad7e44b96ba60565ed72fd00313bd5539879bde7385d41c6935ab34ee12b3b59e8486059bd9b0fc8d58ba3b0b293fefde'
    JWT_SECRET_KEY = 'ZWNjMDJjN2E0ZmU1MTJlZDZlNTI1M2E2NTA3NDJhZWYwMDYzNjk2N2RjMDczNjQ1OWRhZDcxNjM0MWYxNzI5OWRkYjE4NDIxYzQ0MzY1YTBhZTQ2Y2NhNjRjYTVmNWZhYWEyYjVkYzRmMjIwYTExZGRlYTA0NzA4ZWQyODdhMDk='
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
