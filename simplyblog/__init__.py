from dotenv import load_dotenv
from flask import Flask, jsonify, abort
import psycopg2

app=Flask(__name__)

load_dotenv() 

connection = psycopg2.connect(
    database="simply_blog",
    user="postgres",
    password="something123",
    host="44.201.206.16",
    port="5432"
)

cursor = connection.cursor()

# cursor.execute("create table if not exists posts (id serial primary key, title varchar);")
cursor.execute("drop table if exists books;")
print("sheesh")
connection.commit()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nice", methods=["GET"])
def nice():
    return "<h1>help</h1>"