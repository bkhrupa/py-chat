import os
from dotenv import dotenv_values

class Config:
    DEBUG = True
    APP_NAME = 'My App'
    APP_KEY = None
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database/database.sqlite')
    SECRET_KEY = 'secReT'

    def __init__(self):
        config = dotenv_values()

        self.APP_NAME = config['APP_NAME']
        self.SECRET_KEY = config['SECRET_KEY']


if (__name__ == '__main__'):
    config = Config()

    # OS_ENV = os.getenv('APP_NAME')
    #
    print(config.APP_NAME)
    # print(OS_ENV)
    # print(os.getenv('APP'))
    # print(os.getenv('APP_KEY'))
