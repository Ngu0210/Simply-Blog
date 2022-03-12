from flask import Blueprint
from main import db

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def create_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables Deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.User import User
    from models.Post import Post
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker()
    users = []

    for i in range(5):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)
        
    print(f"{i} user record(s) created")

    db.session.commit()

    for i in range(10):
        post = Post()
        post.title = faker.name()
        post.content = faker.text()
        post.user_id = random.choice(users).id

        db.session.add(post)
    print(f"{i} user post(s) created")

    db.session.commit()
    print("Tables seeded")
    
