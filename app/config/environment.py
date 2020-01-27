import os

from . import private_config

# SITE_URL = 'https://www.undyingkingdoms.com'

MYSQL_BASE = "mysql+mysqldb://{user}:{passwd}@{host}/{dbname}?{options}"
USER = os.environ["MYSQL_USER"]
DB_PASSWORD = os.environ["MYSQL_PASSWORD"]
DATABASE_NAME = os.environ["MYSQL_DATABASE"]
HOST = os.environ["MYSQL_HOST"] # docker-compose service name?
OPTIONS = "charset=utf8"

# dummy account info
JACOB_TEMPORARY_EMAIL = "elthran@gmail.com"
JACOB_TEMPORARY_ACCOUNT_PASSWORD = "star"
MARLEN_TEMPORARY_EMAIL = "haldon@gmail.com"
MARLEN_TEMPORARY_ACCOUNT_PASSWORD = "brunner"


class BaseConfig:
    """Base configuration."""
    ENV = 'base'
    SECRET_KEY = private_config.SECRET_KEY
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    THREADS_PER_PAGE = 2
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # I don't know what these do but we might need them at some point.
    # from server show global variables like '%connections%';
    SQLALCHEMY_POOL_SIZE = 5000
    SQLALCHEMY_POOL_RECYCLE = 30 * 60  # 30 minutes, sounded reasonable?
    # sounded reasonable, maybe should be same as SQLALCHEMY_POOL_RECYCLE
    SQLALCHEMY_POOL_TIMEOUT = 30

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = private_config.CSRF_SESSION_KEY


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_POOL_RECYCLE = 299  # 1s less than PythonAnywhere's 300s (5 min).
    SQLALCHEMY_DATABASE_URI = private_config.SERVER_DATABASE_URI


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
    if DEBUG:
        SSLIFY_DISABLE = True
    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(
        user=USER, passwd=DB_PASSWORD, host=HOST, dbname=DATABASE_NAME, options=OPTIONS)


class TestingConfig:
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = MYSQL_BASE.format(
        user=USER, passwd=DB_PASSWORD, host=HOST, dbname=DATABASE_NAME + '_test', options=OPTIONS)
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

    # show all sql queries
    # SQLALCHEMY_ECHO = True
