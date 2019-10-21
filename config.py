import os

class Config:
    
      
    '''
    Describes the general configurations
    
    '''
    
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:brayo13@localhost/pitch'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
   
  
    
    
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
        
    