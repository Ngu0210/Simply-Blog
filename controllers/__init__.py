from controllers.posts_controller import posts
from controllers.auth_controller import auth
from controllers.userImage_controller import userImages
from controllers.home_controller import index
from controllers.swagger_controller import swag

registerable_controllers = [
    posts,
    auth,
    userImages,
    index,
    swag,
]