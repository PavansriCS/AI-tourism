from flask import Blueprint

from controllers.notification_controller import list_notifications

notification_bp = Blueprint("notifications", __name__)
notification_bp.get("")(list_notifications)
notification_bp.get("/")(list_notifications)

