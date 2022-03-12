import os
from pickle import TRUE

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set!")

        return value

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    Testing = True
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI_TEST")

        if not value:
            raise ValueError("DB_URI is not set!")

        return value


environment = os.getenv("FLASK_ENV")

if environment == "production":
    app_config = TestingConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()