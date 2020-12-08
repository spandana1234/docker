import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', b'fr\xb2\xa8\xfa\xbf{\x95\x0b0}M')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://spandana:spandanaabc@192.168.43.108/spandana_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://spandana:spandanaabc@192.168.43.108/spandana_db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://spandana:spandanaabc@192.168.43.108/spandana_db'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
