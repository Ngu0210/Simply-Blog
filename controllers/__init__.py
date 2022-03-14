from controllers.posts_controller import posts
from controllers.auth_controller import auth
from controllers.userImage_controller import userImages
from controllers.home_controller import index

registerable_controllers = [
    posts,
    auth,
    userImages,
    index,
]