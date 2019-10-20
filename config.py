import os

class Config:
    
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
        
    