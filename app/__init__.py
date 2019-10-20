from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig


bootstrap = Bootstrap()
db = SQLAlchemy()



def create_app(config_name):
    
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    # Setting up configuration
    app.config.from_object(DevConfig)
    
    
    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app