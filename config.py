import os

class Config:
    
    '''
    Describes the general configurations
    
    '''
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}
    