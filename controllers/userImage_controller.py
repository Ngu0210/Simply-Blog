from flask import Blueprint, request, jsonify, abort, current_app, Response
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.UserImage import UserImage
from models.User import User
from schemas.UserImageSchema import userImage_schema
import boto3
from main import db
from pathlib import Path

userImages = Blueprint("userImages", __name__, url_prefix="/users/<int:user_id>/image")

@userImages.route("/", methods=["POST"])
@jwt_required()
@verify_user
def userImage_create(user_id, user=None):
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return abort(401, description="Invalid User")

    if "image" not in request.files:
        return abort(401, description="No Image")

    image = request.files["image"]

    if Path(image.filename).suffix not in [".png", ".jpeg", ".JPG"]:
        return abort(400, description="Invalid file type    ")

    filename = f"{user_id}{Path(image.filename).suffix}"

    print(current_app.config["AWS_S3_BUCKET"])

    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    key = f"user_images/{filename}"

    bucket.upload_fileobj(image, key)

    if not user.user_image:
        new_image = UserImage()
        new_image.filename = filename
        user.user_image = new_image
        db.session.commit()

    return ("", 201)


@userImages.route("/<int:id>", methods=["GET"])
@jwt_required()
@verify_user
def userImage_show(user_id, id, user=None):
    user_image = UserImage.query.filter_by(id=id).first()

    if not user_image:
        return abort(401, description="Image Not Found")
    
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    filename = user_image.filename
    file_obj = bucket.Object(f"user_images/{filename}").get()

    return Response(
        file_obj["Body"].read(),
        mimetype="image/*",
        headers={"Content-Disposition": "attachment;filename=image"}
    )


@userImages.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@verify_user
def userImage_delete(user_id, id, user=None):
    user = UserImage.query.filter_by(id=user_id).first()

    if not user:
        return abort(401, description="Invalid User")

    print(user.user_image)

    if user.user_image:
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        filename = user.user_image.filename

        bucket.Object(f"user_images/{filename}").delete()

        db.session.delete(user.user_image)
        db.session.commit()

    return ("", 204)