from database import cursor, connection
from flask import Blueprint, request, jsonify

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/", methods=["GET"])
def user_index():
    return "all posts"