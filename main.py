from dotenv import load_dotenv
from flask import Flask, render_template
from users import users

app=Flask(__name__)
load_dotenv() 

app.register_blueprint(users)

