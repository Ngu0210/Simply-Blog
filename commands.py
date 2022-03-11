from flask import Blueprint
from main import db

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("dannynguyen")
def danny():
    print("Hello world!")

