# Load up Environment Variables
from dotenv import load_dotenv
load_dotenv() 

# Init Flask
from flask import Flask, render_template
app = Flask(__name__) 

# Init ORM Database
from database import init_db
db = init_db(app) 

#Setup Serialization and Deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

# Register Controllers
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)

