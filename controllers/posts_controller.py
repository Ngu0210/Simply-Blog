from database import cursor, connection
from flask import Blueprint, request, jsonify

users = Blueprint("posts", __name__, url_prefix="/posts")

@users.route("/", methods=["GET"])
def user_index():
    return "all posts"