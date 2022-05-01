from instance.config import NEWS_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

     '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    '''
    DEBUG = True
