import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    #SECRET = os.getenv('SECRET')
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    HOST="0.0.0.0"
    SECRET="springboard"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost/loan'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:password@localhost/loan'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:password@localhost/loan'
    DEBUG = True


app_config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
}
