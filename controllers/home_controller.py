from flask import render_template, Blueprint

index = Blueprint("home", __name__,)

@index.route("/")
@index.route("/home")
def home():
    #Index page
    print("help")
    return render_template("home.html", title="Simply Blog")