from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from database.mongo import get_db
from utils.serializers import clean_list


@jwt_required()
def list_trips():
    trips = clean_list(get_db()["trips"].find({"userId": get_jwt_identity()}))
    return jsonify({"trips": trips})

