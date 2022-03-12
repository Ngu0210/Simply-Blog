# Load up Environment Variables
from dotenv import load_dotenv
load_dotenv() 

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager



db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__) 
    app.config.from_object("default_settings.app_config")

    # Init ORM Database
    db.init_app(app)

    #Setup Serialization and Deserialization
    ma.init_app(app)

    #Setup Encryption
    bcrypt.init_app(app)

    #Token Manager
    jwt.init_app(app)

    #Setup Marshmallow Validation Handling
    from marshmallow.exceptions import ValidationError

    #Setup CLI commands
    from commands import db_commands
    app.register_blueprint(db_commands)

    # Register Controllers
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)


    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400 )

    return app
