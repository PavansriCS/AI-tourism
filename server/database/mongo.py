import os
from typing import Optional

from flask import current_app, g
from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError

from database.seed_data import COLLECTIONS

client: Optional[MongoClient] = None
database = None
mongo_available = False


def init_db(app):
    global client, database, mongo_available
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME", "all_tourism_assistant")
    mongo_available = False

    if uri and not uri.startswith("mongodb+srv://username"):
        try:
            client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            client.admin.command("ping")
            database = client[db_name]
            mongo_available = True
            app.logger.info("Connected to MongoDB database %s", db_name)
            ensure_seed_data(database)
            return
        except ServerSelectionTimeoutError as exc:
            app.logger.warning("MongoDB connection unavailable: %s", exc)
        except PyMongoError as exc:
            app.logger.warning("MongoDB error: %s", exc)

    database = InMemoryDatabase(COLLECTIONS)
    app.logger.warning("Using in-memory data store. Configure MONGO_URI for MongoDB Atlas persistence.")


def get_db():
    if "db" not in g:
        g.db = database
    return g.db


def ensure_seed_data(db):
    for name, rows in COLLECTIONS.items():
        if db[name].count_documents({}) == 0:
            db[name].insert_many(rows)


class InMemoryDatabase:
    def __init__(self, collections):
        self.collections = {name: InMemoryCollection(rows) for name, rows in collections.items()}

    def __getitem__(self, name):
        if name not in self.collections:
            self.collections[name] = InMemoryCollection([])
        return self.collections[name]


class InMemoryCollection:
    def __init__(self, rows):
        self.rows = [dict(row) for row in rows]

    def find(self, query=None, projection=None):
        query = query or {}
        return [row for row in self.rows if self._match(row, query)]

    def find_one(self, query=None):
        query = query or {}
        for row in self.rows:
            if self._match(row, query):
                return dict(row)
        return None

    def insert_one(self, document):
        self.rows.append(dict(document))
        return type("InsertOneResult", (), {"inserted_id": document.get("_id") or document.get("id")})()

    def insert_many(self, documents):
        for document in documents:
            self.insert_one(document)

    def update_one(self, query, update, upsert=False):
        row = self.find_one(query)
        if row:
            target = next(item for item in self.rows if item.get("id") == row.get("id") or item.get("email") == row.get("email"))
            target.update(update.get("$set", {}))
            for key, value in update.get("$push", {}).items():
                target.setdefault(key, []).append(value)
        elif upsert:
            self.rows.append({**query, **update.get("$set", {})})

    def count_documents(self, query):
        return len(self.find(query))

    def _match(self, row, query):
        for key, expected in query.items():
            value = row.get(key)
            if isinstance(expected, dict) and "$regex" in expected:
                if expected["$regex"].lower() not in str(value).lower():
                    return False
            elif value != expected:
                return False
        return True
