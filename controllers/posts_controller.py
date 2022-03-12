
from flask import Blueprint, request, jsonify, abort
from main import db
from models.Post import Post
from models.User import User
from schemas.PostSchema import posts_schema, post_schema
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/", methods=["GET"])
def user_index():
    # Return all users
    posts = Post.query.options(joinedload("user")).all()
    return jsonify(posts_schema.dump(posts))

@posts.route("/", methods=["POST"])
@jwt_required()
@verify_user
def user_create(user=None):
    # Create a new user
    post_fields = post_schema.load(request.json)

    new_post = Post()
    new_post.title = post_fields["title"]
    new_post.content = post_fields["content"]
    
    user.posts.append(new_post)

    db.session.commit() 

    return jsonify(post_schema.dump(new_post))

@posts.route("/<int:id>", methods=["GET"])
def user_show(id):
    # Return a single user
    post = Post.query.get(id)
    return jsonify(post_schema.dump(post))

@posts.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required()
@verify_user
def user_update(id, user=None):
    # Update a user
    post_fields = post_schema.load(request.json)
    
    post = Post.query.filter_by(id=id, user_id=user.id)
    
    if post.count() != 1:
        return abort(401, description="Unauthorized to update this book")

    post.update(post_fields)

    db.session.commit()

    return jsonify(post_schema.dump(post[0]))

@posts.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@verify_user
def user_delete(id, user=None):
    # Delete a user

    post = Post.query.filter_by(id=id, user_id=user.id).first()

    if not post:
        return abort(404)

    db.session.delete(post)
    db.session.commit()

    return jsonify(post_schema.dump(post))