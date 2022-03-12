from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.UserImage import UserImage
from models.User import User
from schemas.UserImageSchema import userImage_schema

userImages = Blueprint("userImages", __name__, url_prefix="/users/<int:user_id>/image")

@userImages.route("/", methods=["POST"])
@jwt_required()
@verify_user
def userImage_create(user_id, user=None):
    if "image" in request.files:
        image = request.files["image"]
        image.save("uploaded_images/file_1")
        return ("", 200)

@userImages.route("/<int:id>", methods=["GET"])
@jwt_required()
@verify_user
def userImage_show(user_id, id, user=None):
    return "2"

@userImages.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@verify_user
def userImage_delete(user_id, user=None):
    return "3"