import os

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://brian: stephen13@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
   
    
    '''
    Describes the general configurations
    
    '''
    
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
class DevConfig(Config):
    

    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}
        
    