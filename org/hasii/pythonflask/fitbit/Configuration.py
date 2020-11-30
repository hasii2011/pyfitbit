import os


basedir = os.getenv("DB_PATH")


class Configuration(object):
    """"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or '6*TEAd%nb,L$jJxj'

    if basedir is None:
        raise AssertionError("SQL Lite DB_PATH not set")

    SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'fitbit.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
