from main import ma
from models.Post import Post
from schemas.UserSchema import UserSchema
# from flask_marshmallow.fields import Nested

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post

    title = ma.String(required=True)
    content = ma.String(required=True)
    user = ma.Nested(UserSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)