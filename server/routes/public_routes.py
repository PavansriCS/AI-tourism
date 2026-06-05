from flask import Blueprint

from controllers.public_controller import adventure_parks, attractions, destination_details, home, hotels, resorts, restaurants, safety, search, water_parks

public_bp = Blueprint("public", __name__)
public_bp.get("/public/home")(home)
public_bp.get("/search")(search)
public_bp.get("/destinations/<slug>")(destination_details)
public_bp.get("/hotels")(hotels)
public_bp.get("/resorts")(resorts)
public_bp.get("/restaurants")(restaurants)
public_bp.get("/attractions")(attractions)
public_bp.get("/water-parks")(water_parks)
public_bp.get("/adventure-parks")(adventure_parks)
public_bp.get("/safety")(safety)
