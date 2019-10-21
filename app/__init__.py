from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options, DevConfig



db = SQLAlchemy()



def create_app(config_name):
    
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    
     # Initializing flask extensions
    db.init_app(app)
    # Setting up configuration
    app.config.from_object(DevConfig)
    
    
    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #registering the auth blueprint
    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix = '/auth')
    
    return app