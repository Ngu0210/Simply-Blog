from main import db

class UserImage(db.Model):
    __tablename__ = "user_images"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(), nullable=False, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<UserImage {self.filename}>"