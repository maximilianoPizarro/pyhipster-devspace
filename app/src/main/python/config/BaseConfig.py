
import os
from datetime import timedelta
import tempfile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    # Flask 
    ENV = 'development'
    FLASK_ENV = 'development'
    SECRET_KEY = '26ce0e791336a0810d942a0f651cdcd5c718e55fab63d6b4c3e9d46f553098353b8d0bfb7724f4a36a44e4d515aa3cbbefc8'
    JWT_SECRET_KEY = 'ZTkwMzhlNDVlMzAxZWQ2NDFjMjZjNGQyODA3ZGUyMTdmZTM0MDJiZDhmMzAwZjViMzk2YmVlNTUwY2U5NTM2MmYyZDFlNDhlNDc0MDY2ZDBkNTU4ZWQ4NGExMmJkMWYyYjA3NTFhMjE2ZTJjZmE3YzEzNjQxOGI0Y2JjZDJiNDE='
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
    SECRET_KEY = '26ce0e791336a0810d942a0f651cdcd5c718e55fab63d6b4c3e9d46f553098353b8d0bfb7724f4a36a44e4d515aa3cbbefc8'
    JWT_SECRET_KEY = 'ZTkwMzhlNDVlMzAxZWQ2NDFjMjZjNGQyODA3ZGUyMTdmZTM0MDJiZDhmMzAwZjViMzk2YmVlNTUwY2U5NTM2MmYyZDFlNDhlNDc0MDY2ZDBkNTU4ZWQ4NGExMmJkMWYyYjA3NTFhMjE2ZTJjZmE3YzEzNjQxOGI0Y2JjZDJiNDE='
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
