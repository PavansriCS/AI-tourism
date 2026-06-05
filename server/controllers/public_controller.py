from flask import jsonify, request

from ai.recommendation_engine import build_recommendations
from database.mongo import get_db
from database.seed_data import SAFETY
from utils.serializers import clean_document, clean_list


def normalize_destination(item):
    if not item:
        return item
    return {
        **item,
        "id": item.get("id") or item.get("_id"),
        "slug": item.get("slug") or str(item.get("name", "")).lower().replace(" ", "-"),
        "city": item.get("name"),
        "image": item.get("image") or item.get("imageUrl"),
        "location": f"{item.get('name')}, {item.get('state')}",
        "rating": item.get("rating", 4.4),
        "interests": item.get("interests", [item.get("category", "Tourism")])
    }


def normalize_listing(item, destinations_by_id):
    if not item:
        return item
    destination = destinations_by_id.get(item.get("destinationId"), {})
    price = item.get("priceRange")
    if not price and item.get("pricePerNight") is not None:
        price = f"Rs. {item.get('pricePerNight')} per night"
    if not price and item.get("priceForTwo") is not None:
        price = f"Rs. {item.get('priceForTwo')} for two"
    if not price and item.get("entryFee") is not None:
        price = "Free" if item.get("entryFee") == 0 else f"Rs. {item.get('entryFee')}"
    address = item.get("address") or item.get("location") or destination.get("name")
    return {
        **item,
        "id": item.get("id") or item.get("_id"),
        "destination": destination.get("name") or item.get("destination"),
        "city": destination.get("name"),
        "state": destination.get("state"),
        "location": address,
        "address": address,
        "image": item.get("image") or item.get("imageUrl"),
        "priceRange": price or "Check official site",
        "description": item.get("description") or f"Recommended listing near {destination.get('name', 'this destination')}.",
        "officialWebsite": item.get("officialWebsite") or destination.get("officialWebsite") or item.get("bookingUrl"),
        "bookingTier": item.get("bookingTier") or "Standard",
        "bookingProvider": item.get("bookingProvider") or "Official provider",
        "providerContact": item.get("providerContact") or item.get("providerHelpUrl") or item.get("officialWebsite") or destination.get("officialWebsite"),
        "providerHelpUrl": item.get("providerHelpUrl") or item.get("providerContact") or item.get("officialWebsite") or destination.get("officialWebsite"),
        "googleMapsUrl": destination.get("googleMapsUrl"),
        "facilities": item.get("facilities") or [item.get("category", "Tourism")],
        "distance": f"{item.get('distanceKm')} km" if item.get("distanceKm") is not None else item.get("distance")
    }


def destination_lookup(db):
    destinations = [normalize_destination(item) for item in clean_list(db["destinations"].find())]
    return destinations, {item.get("_id") or item.get("id"): item for item in destinations}


def home():
    db = get_db()
    destinations, lookup = destination_lookup(db)
    return jsonify({
        "destinations": destinations[:9],
        "hotels": [normalize_listing(item, lookup) for item in clean_list(db["resorts"].find())[:3]],
        "restaurants": [normalize_listing(item, lookup) for item in clean_list(db["restaurants"].find())[:3]],
        "attractions": [normalize_listing(item, lookup) for item in clean_list(db["attractions"].find())[:3]],
        "waterParks": [],
        "adventureParks": []
    })


def search():
    db = get_db()
    destination = request.args.get("destination", "")
    budget = request.args.get("budget", 25000)
    days = request.args.get("days", 4)
    interests = request.args.get("interests", "")
    key = destination.lower().strip()
    words = [word for word in key.replace("-", " ").split() if len(word) > 2]
    known_destinations, lookup = destination_lookup(db)
    destination_hint = next((item["name"].lower() for item in known_destinations if item["name"].lower() in key), "")
    destination_id_hint = next((item["id"] for item in known_destinations if item["name"].lower() == destination_hint), "")

    def match(rows):
        if not key:
            return rows
        matched = []
        for item in rows:
            related_destination = lookup.get(item.get("destinationId"), {})
            haystack = " ".join(str(value) for value in [
                item.get("name", ""),
                item.get("destination", ""),
                item.get("city", ""),
                item.get("location", ""),
                item.get("address", ""),
                related_destination.get("name", ""),
                related_destination.get("state", ""),
                related_destination.get("category", "")
            ]).lower()
            if destination_hint and destination_hint in haystack:
                matched.append(item)
            elif destination_id_hint and item.get("destinationId") == destination_id_hint:
                matched.append(item)
            elif key in haystack or any(word in haystack for word in words):
                matched.append(item)
        return matched

    destinations = match(known_destinations)
    hotels = [normalize_listing(item, lookup) for item in match(clean_list(db["hotels"].find()))]
    resorts = [normalize_listing(item, lookup) for item in match(clean_list(db["resorts"].find()))]
    restaurants = [normalize_listing(item, lookup) for item in match(clean_list(db["restaurants"].find()))]
    attractions = [normalize_listing(item, lookup) for item in match(clean_list(db["attractions"].find()))]

    return jsonify({
        "destinations": destinations,
        "hotels": sort_by_budget(hotels, budget),
        "resorts": sort_by_budget(resorts, budget),
        "restaurants": sort_by_budget(restaurants, budget),
        "attractions": sort_by_budget(attractions, budget),
        "waterParks": [],
        "adventureParks": [],
        "recommendations": build_recommendations(destination, budget, days, interests)
    })


def destination_details(slug):
    db = get_db()
    destinations, lookup = destination_lookup(db)
    destination = next((item for item in destinations if item.get("slug") == slug or item.get("id") == slug), None)
    if not destination:
        return jsonify({"message": "Destination not found"}), 404
    hotels = [normalize_listing(item, lookup) for item in clean_list(db["hotels"].find({"destinationId": destination["id"]}))]
    resorts = [normalize_listing(item, lookup) for item in clean_list(db["resorts"].find({"destinationId": destination["id"]}))]
    restaurants = [normalize_listing(item, lookup) for item in clean_list(db["restaurants"].find({"destinationId": destination["id"]}))]
    attractions = [normalize_listing(item, lookup) for item in clean_list(db["attractions"].find({"destinationId": destination["id"]}))]
    return jsonify({
        "destination": destination,
        "hotels": hotels + resorts,
        "restaurants": restaurants,
        "attractions": attractions,
        "waterParks": [],
        "adventureParks": []
    })


def hotels():
    db = get_db()
    _, lookup = destination_lookup(db)
    return jsonify({
        "hotels": sort_by_budget([normalize_listing(item, lookup) for item in clean_list(db["hotels"].find())], request.args.get("budget", 25000)),
        "resorts": sort_by_budget([normalize_listing(item, lookup) for item in clean_list(db["resorts"].find())], request.args.get("budget", 25000))
    })


def resorts():
    db = get_db()
    _, lookup = destination_lookup(db)
    return jsonify({"resorts": sort_by_budget([normalize_listing(item, lookup) for item in clean_list(db["resorts"].find())], request.args.get("budget", 25000))})


def restaurants():
    db = get_db()
    _, lookup = destination_lookup(db)
    return jsonify({"restaurants": sort_by_budget([normalize_listing(item, lookup) for item in clean_list(db["restaurants"].find())], request.args.get("budget", 25000))})


def attractions():
    db = get_db()
    _, lookup = destination_lookup(db)
    return jsonify({"attractions": sort_by_budget([normalize_listing(item, lookup) for item in clean_list(db["attractions"].find())], request.args.get("budget", 25000))})


def water_parks():
    return jsonify({"waterParks": []})


def adventure_parks():
    return jsonify({"adventureParks": []})


def safety():
    return jsonify(SAFETY)


def numeric_price(item):
    for key in ("pricePerNight", "priceForTwo", "entryFee"):
        if item.get(key) is not None:
            return float(item.get(key) or 0)
    text = str(item.get("priceRange", "999999"))
    digits = "".join(char if char.isdigit() else " " for char in text).split()
    return float(digits[0]) if digits else 999999.0


def sort_by_budget(items, budget):
    try:
        budget_value = float(budget or 25000)
    except (TypeError, ValueError):
        budget_value = 25000.0
    per_item_budget = max(500, budget_value * 0.35)
    return sorted(
        items,
        key=lambda item: (
            numeric_price(item) > per_item_budget,
            numeric_price(item),
            float(item.get("distanceKm") or 99),
            -float(item.get("rating") or 0)
        )
    )
