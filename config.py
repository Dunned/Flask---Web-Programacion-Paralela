from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587  # TLS
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME')
    #MAIL_PASSWORD = 'progra123'
    MAIL_PASSWORD = config('MAIL_PASSWORD')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
