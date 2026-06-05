from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from database.mongo import get_db
from middleware.auth import current_user
from models.user import create_user_document, public_user, verify_password
from utils.validators import require_fields


def signup():
    payload = request.get_json(silent=True) or {}
    error = require_fields(payload, ["name", "email", "password"])
    if error:
        return jsonify({"message": error}), 400
    db = get_db()
    email = payload["email"].strip().lower()
    if db["users"].find_one({"email": email}):
        return jsonify({"message": "Email already registered"}), 409
    user = create_user_document(payload)
    db["users"].insert_one(user)
    token = create_access_token(identity=user["id"])
    return jsonify({"token": token, "user": public_user(user)}), 201


def login():
    payload = request.get_json(silent=True) or {}
    error = require_fields(payload, ["email", "password"])
    if error:
        return jsonify({"message": error}), 400
    user = get_db()["users"].find_one({"email": payload["email"].strip().lower()})
    if not user or not verify_password(user, payload["password"]):
        return jsonify({"message": "Invalid email or password"}), 401
    token = create_access_token(identity=user["id"])
    return jsonify({"token": token, "user": public_user(user)})


@jwt_required()
def me():
    return jsonify({"user": public_user(current_user())})

