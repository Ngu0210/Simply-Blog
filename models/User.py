from main import db
from models.UserImage import UserImage

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    age = db.Column(db.String())

    posts = db.relationship("Post", backref="user", lazy="dynamic")
    user_image = db.relationship("UserImage", backref="user", uselist=False)

    def __repr__(self):
        return f"<User {self.email}>"