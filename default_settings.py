import os
from pickle import TRUE

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "123456"

class DevelopmentConfig(Config):
    DEBUG = True
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.getenv("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set!")

        return value

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.getenv("JWT_SECRET_KEY")

        if not value:
            raise ValueError("JWT_SECRET_KEY is not set!")

        return value

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