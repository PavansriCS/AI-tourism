from flask import Blueprint

from controllers.trip_controller import list_trips

trip_bp = Blueprint("trips", __name__)
trip_bp.get("")(list_trips)
trip_bp.get("/")(list_trips)

