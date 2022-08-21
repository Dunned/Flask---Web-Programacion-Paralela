import imp
from decouple import config


class Config:
    SECRET_KEY = 'programacion_paralela2022'


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587  # TLS
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pruebaparalela2022@gmail.com'
    #MAIL_PASSWORD = 'progra123'
    MAIL_PASSWORD = 'ptmbauixzvptsamv'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
