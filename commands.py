from flask import Blueprint
from main import db

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def create_db():
    db.drop_all()
    print("Tables Deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.User import User
    from faker import Faker
    faker = Faker()

    for i in range(10):
        user = User()
        user.firstname = faker.first_name()
        user.lastname = faker.last_name()

        db.session.add(user)
        print(f"{i} user record(s) created")

    db.session.commit()
    print("Tables seeded")
    

        db.session.add(user)
        print(f"{i} user record(s) created")

    db.session.commit()
    print("Tables seeded")
    
