from database.seed_data import ATTRACTIONS, DESTINATIONS, HOTELS, RESORTS, RESTAURANTS


def build_recommendations(destination="", budget=25000, days=4, interests=""):
    budget = _number(budget, 25000)
    days = int(_number(days, 4))
    interest_words = [item.strip().lower() for item in str(interests).replace(",", " ").split() if item.strip()]
    selected = _rank_destinations(str(destination), interest_words)[0]

    hotels = _rank_listings(HOTELS, selected["_id"], budget, interest_words, days)
    resorts = _rank_listings(RESORTS, selected["_id"], budget, interest_words, days)
    restaurants = _rank_listings(RESTAURANTS, selected["_id"], budget, interest_words, days)
    attractions = _rank_listings(ATTRACTIONS, selected["_id"], budget, interest_words, days)
    daily_budget = max(1500, int(budget // max(days, 1)))

    return {
        "destination": selected["name"],
        "places": [item["name"] for item in attractions[:5]],
        "touristAttractions": [item["name"] for item in attractions[:5]],
        "hotels": [item["name"] for item in hotels[:3]],
        "resorts": [item["name"] for item in resorts[:3]],
        "restaurants": [item["name"] for item in restaurants[:3]],
        "waterThemeParks": [],
        "adventureParks": [item["name"] for item in attractions if "tour" in item.get("category", "").lower()][:3],
        "activities": _activity_suggestions(selected, interest_words),
        "budgetTips": [
            f"Your daily planning target is around Rs. {daily_budget}.",
            "Budget hotels and low-cost attractions are ranked before luxury stays.",
            "Use Book Now only to continue on official external provider websites."
        ],
        "routeSuggestions": [
            f"Start from central {selected['name']} and group nearby attractions by distance.",
            "Keep farther attractions for the middle day of the trip.",
            "Use Google Maps navigation before each transfer."
        ],
        "bookingOptions": {
            "hotels": [{"name": item["name"], "bookingUrl": item["bookingUrl"]} for item in hotels[:3]],
            "resorts": [{"name": item["name"], "bookingUrl": item["bookingUrl"]} for item in resorts[:3]],
            "attractions": [{"name": item["name"], "bookingUrl": item["bookingUrl"]} for item in attractions[:3]]
        }
    }


def build_trip_plan(destination, budget, days, interests):
    recommendations = build_recommendations(destination, budget, days, interests)
    days = int(_number(days, 3))
    budget = int(_number(budget, 25000))
    places = recommendations["places"] or ["Local market", "Scenic viewpoint", "Cultural landmark"]
    restaurants = recommendations["restaurants"] or ["Recommended local restaurant"]
    schedule = []

    for index in range(days):
        place = places[index % len(places)]
        food = restaurants[index % len(restaurants)]
        schedule.append({
            "day": index + 1,
            "theme": _theme(index, recommendations["destination"]),
            "items": [
                {"time": "08:30", "duration": "2h", "activity": f"Visit {place}", "route": "Start with the closest attraction to reduce transport cost."},
                {"time": "12:30", "duration": "1h 30m", "activity": f"Lunch at {food}", "route": "Pick a restaurant near the morning attraction."},
                {"time": "15:00", "duration": "2h", "activity": "Nearby low-cost attraction cluster", "route": "Prioritize nearby points before premium experiences."},
                {"time": "19:00", "duration": "2h", "activity": "Safe evening return", "route": "Use official taxis, hotel pickup, or public transport corridors."}
            ]
        })

    return {
        "destination": recommendations["destination"],
        "days": days,
        "estimatedBudget": budget,
        "interests": interests,
        "routeSuggestions": recommendations["routeSuggestions"],
        "nearbyAttractions": recommendations["places"],
        "bookingOptions": recommendations["bookingOptions"],
        "schedule": schedule
    }


def _rank_destinations(query, interest_words):
    query = query.lower().replace("-", " ")
    words = [word for word in query.split() if len(word) > 2]
    scored = []
    for item in DESTINATIONS:
        haystack = " ".join([item["name"], item["state"], item["category"], item["budgetCategory"]]).lower()
        score = 0
        if item["name"].lower() in query or query in item["name"].lower():
            score += 20
        score += sum(6 for word in words if word in haystack)
        score += sum(2 for word in interest_words if word in haystack)
        scored.append((score, item))
    return [item for _, item in sorted(scored, key=lambda pair: pair[0], reverse=True)]


def _rank_listings(items, destination_id, budget, interest_words, days):
    destination_items = [item for item in items if item.get("destinationId") == destination_id]
    per_day_budget = max(500, budget / max(days, 1))
    return sorted(destination_items, key=lambda item: (
        _price(item) > per_day_budget * 0.7,
        _price(item),
        float(item.get("distanceKm") or 99),
        -float(item.get("rating") or 0),
        -_interest_score(item, interest_words)
    ))


def _price(item):
    for key in ("pricePerNight", "priceForTwo", "entryFee"):
        if item.get(key) is not None:
            return float(item.get(key) or 0)
    return 999999.0


def _interest_score(item, interest_words):
    haystack = " ".join(str(value) for value in item.values()).lower()
    return sum(1 for word in interest_words if word in haystack)


def _number(value, fallback):
    try:
        return float(str(value).replace("₹", "").replace("Rs.", "").replace(",", "").strip())
    except (TypeError, ValueError):
        return float(fallback)


def _activity_suggestions(destination, interest_words):
    base = [
        f"Explore {destination['name']} signature attractions",
        "Choose budget stays first, then upgrade only if budget remains",
        "Use official booking pages for hotels, resorts, and guided experiences"
    ]
    joined = " ".join(interest_words)
    if "food" in joined:
        base.insert(0, "Add one local cuisine stop each day")
    if "adventure" in joined:
        base.insert(0, "Keep guided outdoor activities in daylight hours")
    if "heritage" in joined or "culture" in joined:
        base.insert(0, "Start heritage sites early before crowds")
    return base[:5]


def _theme(index, destination):
    themes = ["Arrival and budget orientation", "Signature attractions", "Food and culture", "Nearby experiences", "Flexible buffer day"]
    return f"{themes[index % len(themes)]} in {destination}"
