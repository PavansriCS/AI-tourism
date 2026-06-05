from datetime import datetime, timezone
from uuid import uuid4

from werkzeug.security import check_password_hash, generate_password_hash


def create_user_document(payload):
    return {
        "id": str(uuid4()),
        "name": payload["name"].strip(),
        "email": payload["email"].strip().lower(),
        "passwordHash": generate_password_hash(payload["password"]),
        "homeCity": payload.get("homeCity", "").strip(),
        "createdAt": datetime.now(timezone.utc).isoformat()
    }


def verify_password(user, password):
    return check_password_hash(user.get("passwordHash", ""), password)


def public_user(user):
    if not user:
        return None
    return {
        "id": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
        "homeCity": user.get("homeCity", ""),
        "createdAt": user.get("createdAt")
    }

