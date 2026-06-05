from bson import ObjectId


def clean_document(document):
    if not document:
        return document
    result = dict(document)
    if "_id" in result:
        result["id"] = str(result.pop("_id")) if not result.get("id") else result.get("id")
    return result


def clean_list(documents):
    return [clean_document(document) for document in documents]


def object_id(value):
    try:
        return ObjectId(value)
    except Exception:
        return value

