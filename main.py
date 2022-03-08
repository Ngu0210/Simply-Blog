from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Sheesh!</p>"

@app.route("/stock", methods=["GET"])
def stock():
    return "<h1>STOCKS!!!!</h1>"