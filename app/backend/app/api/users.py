from flask import Blueprint, jsonify, request
from app.models.user import User
from app.extensions import db

users_bp = Blueprint("users", __name__)

@users_bp.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()

    return jsonify([user.to_dict() for user in users])

@users_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password") or not data.get("email"):
        return jsonify({"Error" : "Username, Password and Email are required"}), 401
    
    username = data["username"]
    email = data["email"]
    password = data["password"]

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@users_bp.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)

    return(jsonify({"user": user.to_dict()}))