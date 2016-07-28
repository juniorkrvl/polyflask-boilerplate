from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # import and register main app
    from core import core
    app.register_blueprint(core)
    # ---

    # import and register packages
    # from packages.auth import auth
    # app.register_blueprint(main_blueprint)
    # ---
    
    # Set views folders
    app.template_folder = app.config['TEMPLATES_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']

    return app
