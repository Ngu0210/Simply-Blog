from database import cursor, connection
from flask import Blueprint, request, jsonify

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    # Return all users
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    return jsonify(users)

@users.route("/", methods=["POST"])
def user_create():
    # Create a new user
    sql = "INSERT INTO users (firstName, lastName) values (%s, %s);"
    cursor.execute(sql, (request.json["firstName"], request.json["lastName"]))
    connection.commit()

    sql = "SELECT * FROM users ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    user = cursor.fetchone()
    return jsonify(user)

@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    # Return a single user
    sql = "SELECT * FROM users where id = %s;"
    cursor.execute(sql, (id,))
    user = cursor.fetchone()
    return jsonify(user)

@users.route("/<int:id>", methods=["PUT", "PATCH"])
def user_update(id):
    #Update a user
    sql = "UPDATE users SET firstName = %s, lastName = %s WHERE id = %s;"
    cursor.execute(sql, (request.json["firstName"], request.json["lastName"], id))
    connection.commit()

    sql = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql, (id,))
    user = cursor.fetchone()
    return jsonify(user)

@users.route("/<int:id>", methods=["DELETE"])
def user_delete(id):
    sql = "SELECT * FROM users WHERE id = %s;"
    cursor.execute(sql, (id,))
    user = cursor.fetchone()
    
    if user:
        sql = "DELETE FROM users WHERE id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(user)