# from instance.config import NEWS_API_KEY
import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'
    # NEWS_API_KEY =os.environ.get('NEWS_API_KEY')
    NEWS_API_KEY = 'e9bccdcb8e164e9d8e5420ea88db15c5'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '15412rnk'

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
config_options = {
    'development' :DevConfig,
    'production' :ProdConfig
}
