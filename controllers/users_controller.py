
from flask import Blueprint, request, jsonify, abort
from main import db
from models.User import User
from schemas.UserSchema import users_schema, user_schema

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    # Return all users
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@users.route("/", methods=["POST"])
def user_create():
    # Create a new user
    user_fields = user_schema.load(request.json)

    new_user = User()
    new_user.firstname = user_fields["firstname"]
    new_user.lastname = user_fields["lastname"]

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))

@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    # Return a single user
    user = User.query.get(id)
    return jsonify(user_schema.dump(user))

@users.route("/<int:id>", methods=["PUT", "PATCH"])
def user_update(id):
    # Update a user
    user = User.query.filter_by(id=id)
    
    user_fields = user_schema.load(request.json)
    user.update(user_fields)

    db.session.commit()

    return jsonify(user_schema.dump(user[0]))

@users.route("/<int:id>", methods=["DELETE"])
def user_delete(id):
    # Delete a user
    user = User.query.get(id)

    if not user:
        return abort(404)

    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))