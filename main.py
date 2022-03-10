from dotenv import load_dotenv
from flask import Flask, render_template
import controllers
from controllers.users_controller import users

app=Flask(__name__)
load_dotenv() 

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)

