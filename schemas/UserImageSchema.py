from main import ma
from models.UserImage import UserImage
from marshmallow.validate import Length

class UserImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserImage
    
    filename = ma.String(required=True, validate=Length(min=1))

userImage_schema = UserImageSchema()