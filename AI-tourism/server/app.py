from datetime import timedelta
import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from database.mongo import init_db
from routes.ai_routes import ai_bp
from routes.auth_routes import auth_bp
from routes.notification_routes import notification_bp
from routes.public_routes import public_bp
from routes.trip_routes import trip_bp


load_dotenv()


def allowed_origins():
    configured = os.getenv("CLIENT_ORIGIN", "http://localhost:5173")
    origins = [origin.strip() for origin in configured.split(",") if origin.strip()]
    origins.extend(["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173"])
    return sorted(set(origins))


def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-all-tourism-assistant-change-me-with-32-plus-chars")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
    app.config["JSON_SORT_KEYS"] = False

    CORS(
        app,
        origins=allowed_origins(),
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    )
    JWTManager(app)
    init_db(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(public_bp, url_prefix="/api")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")
    app.register_blueprint(trip_bp, url_prefix="/api/trips")
    app.register_blueprint(notification_bp, url_prefix="/api/notifications")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok", "service": "All Tourism Assistant API"})

    @app.errorhandler(404)
    def not_found(_):
        return jsonify({"message": "Route not found"}), 404

    @app.errorhandler(Exception)
    def server_error(error):
        app.logger.exception(error)
        return jsonify({"message": "Unexpected server error"}), 500

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_ENV") != "production")
