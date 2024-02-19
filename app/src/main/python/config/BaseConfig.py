
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = 'dea7ec6b88b24a75afbf930c715f5240fdb96e3106961ea9b30d7fda8d134579123612ed280ab02e482ff6b7f6185fce3b10'
    JWT_SECRET_KEY = 'M2IyZmQyODZhZGI3NjU1ZDBjN2VjNzQ1ZWNmNzk2OTEwZjZhYTZiZGUxYTkwYmE5MGM4ZWE1OWYyMjEwMmE1NjkxNjBhZWUwMWFkYTUwYmI0NTk4YTllNTBhZGRkYjE0NWVhYTc0OTcxNTk5ZGVjMGRlOWE5MzRkMDI2Y2UwZDE='
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
    SECRET_KEY = 'dea7ec6b88b24a75afbf930c715f5240fdb96e3106961ea9b30d7fda8d134579123612ed280ab02e482ff6b7f6185fce3b10'
    JWT_SECRET_KEY = 'M2IyZmQyODZhZGI3NjU1ZDBjN2VjNzQ1ZWNmNzk2OTEwZjZhYTZiZGUxYTkwYmE5MGM4ZWE1OWYyMjEwMmE1NjkxNjBhZWUwMWFkYTUwYmI0NTk4YTllNTBhZGRkYjE0NWVhYTc0OTcxNTk5ZGVjMGRlOWE5MzRkMDI2Y2UwZDE='
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
