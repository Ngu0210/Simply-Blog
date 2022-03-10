from dotenv import load_dotenv
from flask import Flask, render_template

app=Flask(__name__)
load_dotenv() 

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"



