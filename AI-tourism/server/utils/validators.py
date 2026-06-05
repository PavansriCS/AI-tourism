def require_fields(payload, fields):
    missing = [field for field in fields if not payload.get(field)]
    if missing:
        return f"Missing required fields: {', '.join(missing)}"
    return None


def normalize_destination(value):
    return (value or "").strip().lower()

