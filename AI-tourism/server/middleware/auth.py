from flask_jwt_extended import get_jwt_identity

from database.mongo import get_db
from utils.serializers import clean_document


def current_user():
    user_id = get_jwt_identity()
    user = get_db()["users"].find_one({"id": user_id})
    return clean_document(user)

