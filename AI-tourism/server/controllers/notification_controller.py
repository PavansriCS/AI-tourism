from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from database.mongo import get_db
from utils.serializers import clean_list


@jwt_required()
def list_notifications():
    user_id = get_jwt_identity()
    notifications = clean_list(get_db()["notifications"].find())
    visible = [item for item in notifications if item.get("userId") in ("system", user_id, None)]
    return jsonify({"notifications": visible})

