
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '1caea3fe6bf37635758542ac972685f7ffc78999210be326005695140b75a039d0462e550c956936e60b8a5025c1dc9d22e2'
    JWT_SECRET_KEY = 'OTI4YjQ1MWNlMWE5NjE2OWI5M2FhYjdlYmYyYmEzOGEyOWYwNzI5MDQ2OTE4ZDEzN2UzZDE3ZWU0NzQ3ODA1MTY4NmY1NTVkNTY0MWI1NTUwNGM3NTAxOTgwZjM3ZTgzYjJjMDc2NDZlMzFmZmE2OGE2ODU3N2RlYzdiNTdlMTk='
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
    SECRET_KEY = '1caea3fe6bf37635758542ac972685f7ffc78999210be326005695140b75a039d0462e550c956936e60b8a5025c1dc9d22e2'
    JWT_SECRET_KEY = 'OTI4YjQ1MWNlMWE5NjE2OWI5M2FhYjdlYmYyYmEzOGEyOWYwNzI5MDQ2OTE4ZDEzN2UzZDE3ZWU0NzQ3ODA1MTY4NmY1NTVkNTY0MWI1NTUwNGM3NTAxOTgwZjM3ZTgzYjJjMDc2NDZlMzFmZmE2OGE2ODU3N2RlYzdiNTdlMTk='
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
