# Load up Environment Variables
from dotenv import load_dotenv
load_dotenv() 

# Init Flask
from flask import Flask, render_template, jsonify
app = Flask(__name__) 
app.config.from_object("default_settings.app_config")

# Init ORM Database
from database import init_db
db = init_db(app) 

#Setup Serialization and Deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

#Setup Marshmallow Validation Handling
from marshmallow.exceptions import ValidationError

from commands import db_commands
app.register_blueprint(db_commands)

# Register Controllers
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)


@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages), 400 )
