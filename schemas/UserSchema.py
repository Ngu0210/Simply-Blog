from main import ma
from models.User import User
from marshmallow.validate import Length

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    firstname = ma.String(required=True, validate=Length(min=2))
    lastname = ma.String(required=True, validate=Length(min=2))

user_schema = UserSchema()
users_schema = UserSchema(many=True)