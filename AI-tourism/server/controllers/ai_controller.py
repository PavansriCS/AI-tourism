from datetime import datetime, timezone
from uuid import uuid4

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ai.chatbot import tourism_chat_reply
from ai.recommendation_engine import build_recommendations, build_trip_plan
from database.mongo import get_db
from utils.serializers import clean_list


def recommendations():
    payload = request.get_json(silent=True) or {}
    return jsonify({"recommendations": build_recommendations(**payload)})


@jwt_required()
def trip_plan():
    payload = request.get_json(silent=True) or {}
    plan = build_trip_plan(
        payload.get("destination", ""),
        payload.get("budget", 25000),
        payload.get("days", 3),
        payload.get("interests", "")
    )
    document = {
        "id": str(uuid4()),
        "userId": get_jwt_identity(),
        **plan,
        "createdAt": datetime.now(timezone.utc).isoformat()
    }
    get_db()["trips"].insert_one(document)
    return jsonify({"plan": plan})


@jwt_required()
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "").strip()
    if not message:
        return jsonify({"message": "Message is required"}), 400
    reply = tourism_chat_reply(message)
    now = datetime.now(timezone.utc).isoformat()
    db = get_db()
    user_id = get_jwt_identity()
    db["chatbot_history"].insert_one({"id": str(uuid4()), "userId": user_id, "role": "user", "content": message, "createdAt": now})
    db["chatbot_history"].insert_one({"id": str(uuid4()), "userId": user_id, "role": "assistant", "content": reply, "createdAt": now})
    return jsonify({"reply": reply})


@jwt_required()
def history():
    rows = clean_list(get_db()["chatbot_history"].find({"userId": get_jwt_identity()}))
    return jsonify({"history": [{"role": item["role"], "content": item["content"]} for item in rows[-40:]]})

